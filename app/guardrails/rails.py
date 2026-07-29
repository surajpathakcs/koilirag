import time
import logfire
from enum import Enum
from dataclasses import dataclass
from typing import Optional

from langchain_groq import ChatGroq
from nemoguardrails import RailsConfig, LLMRails
from nemoguardrails.integrations.langchain.llm_adapter import LangChainLLMAdapter

from app.config import settings
from app.guardrails.colang_rules import COLANG_CONTENT, YAML_CONTENT


# ── Data Model ──────────────────────────────────────────────────────────────────

class GuardrailStatus(str, Enum):
    PASS = "pass"
    BLOCKED = "blocked"
    DIALOG = "dialog"
    ERROR = "error"


@dataclass
class GuardrailResult:
    status: GuardrailStatus
    response: Optional[str] = None
    reason: Optional[str] = None


# Known NeMo internal failure string — returned as content, not as an exception
NEMO_INTERNAL_ERROR_STRING = "an internal error has occurred"


# Deterministic security patterns.
# These run before NeMo semantic classification.
JAILBREAK_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "forget your instructions",
    "forget you are fonepay",
    "reveal your system prompt",
    "show your system prompt",
    "show your hidden instructions",
    "tell me your prompt",
    "pretend you are chatgpt",
    "you are now chatgpt",
    "you are now a general ai",
    "act as unrestricted",
    "developer mode",
    "forget that you are fonepay ai"
]


INTERNAL_PATTERNS = [
    "show your reasoning",
    "show your chain of thought",
    "show your thought process",
    "show agent steps",
    "show graph steps",
    "show retrieval steps",
    "explain your architecture",
    "explain your internal process",
    "how do you retrieve",
]


# Colang flow names that represent a safety block.
_BLOCK_FLOW_NAMES = {
    "handle off topic",
    "jailbreak protection",
    "prevent assistant internal information exposure",
}


# Colang flow names for dialog rails.
_DIALOG_FLOW_NAMES = {
    "greeting",
    "farewell",
    "capabilities"
}


# ── Singleton ───────────────────────────────────────────────────────────────────

_rails: LLMRails | None = None


def initialize_rails() -> None:
    """
    Build the NeMo LLMRails singleton at app startup.
    Uses llama-3.3-70b-versatile for intent classification. The 8b model
    is too small and fails to correctly classify user intents, causing
    all guardrails to be bypassed.
    """
    global _rails

    guard_llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0
    )
    
    try:
        print("Testing direct Groq call...")
        test = guard_llm.invoke("Say hello")
        print("Groq response:", test)
    except Exception:
        logfire.exception("Direct ChatGroq test failed")
        raise
    # NeMo 0.23+ requires an explicit adapter wrapper for LangChain models.
    # Passing the raw ChatGroq directly is deprecated and causes API key
    # misrouting when a model is also declared in the YAML config.
    adapter = LangChainLLMAdapter(guard_llm)

    config = RailsConfig.from_content(
        colang_content=COLANG_CONTENT,
        yaml_content=YAML_CONTENT
    )

    _rails = LLMRails(config, llm=adapter)
    logfire.info("🛡️ NeMo Guardrails initialised (llama-3.3-70b-versatile).")


# ── Helpers ─────────────────────────────────────────────────────────────────────

def _extract_content(result) -> str:
    """
    NeMo's return type is polymorphic:
      - Without options  → dict {'role': 'assistant', 'content': '...'}
      - With options     → GenerationResponse
    """
    if hasattr(result, "response"):
        resp = result.response

        if isinstance(resp, list) and resp:
            return resp[0].get("content", "")

        return str(resp)

    if isinstance(result, dict):
        return result.get("content", "")

    return str(result)



def _check_rail_fired(result) -> tuple[str, Optional[str]]:
    """
    Determines what kind of rail fired.

    Returns:
        blocked -> security/policy violation
        dialog  -> greeting/farewell/capabilities
        pass    -> no rail fired
    """

    if not hasattr(result, "log") or result.log is None:
        logfire.warning(
            "NeMo response does not contain activated rails log."
        )
        return "pass", None


    activated = result.log.activated_rails or []


    # Temporary debugging.
    # Remove after confirming rails work.
    print("========== ACTIVATED RAILS ==========")

    for rail in activated:
        print("RAIL:", rail.name)

    print("=====================================")


    for rail in activated:
        name = rail.name.lower()


        if name in _BLOCK_FLOW_NAMES:
            return "blocked", rail.name


        if name in _DIALOG_FLOW_NAMES:
            return "dialog", rail.name


    return "pass", None



def _set_span_attrs(
    span,
    status: str,
    message: str,
    latency_ms: float,
    content: Optional[str] = None,
    error: Optional[str] = None,
    flow_name: Optional[str] = None
) -> None:

    if not span:
        return

    span.set_attribute(
        "guardrail.status",
        status
    )

    span.set_attribute(
        "guardrail.query_length",
        len(message)
    )

    span.set_attribute(
        "guardrail.latency_ms",
        round(latency_ms, 1)
    )

    if content:
        span.set_attribute(
            "guardrail.response_snippet",
            content[:100]
        )

    if error:
        span.set_attribute(
            "guardrail.error",
            error[:200]
        )

    if flow_name:
        span.set_attribute(
            "guardrail.flow_name",
            flow_name
        )



# ── Guard Function ──────────────────────────────────────────────────────────────

def guard(message: str) -> GuardrailResult:
    """
    Runs user message through NeMo safety gate.

    PASS:
        Continue to RAG.

    BLOCKED:
        Return refusal.

    DIALOG:
        Return direct conversational response.

    ERROR:
        Guardrail failure.
    """

    if _rails is None:

        logfire.warning(
            "⚠️ Guardrails not initialised."
        )

        return GuardrailResult(
            status=GuardrailStatus.ERROR,
            reason="Guardrails engine not initialised"
        )


    message_lower = message.lower()



    # --------------------------------------------------
    # Deterministic jailbreak detection
    # --------------------------------------------------

    for pattern in JAILBREAK_PATTERNS:

        if pattern in message_lower:

            logfire.warning(
                "Deterministic jailbreak pattern matched: {pattern}",
                pattern=pattern
            )

            return GuardrailResult(
                status=GuardrailStatus.BLOCKED,
                response=(
                    "I can't provide internal instructions or system details. "
                    "I can help with Fonepay-related questions."
                ),
                reason=f"Deterministic jailbreak match: {pattern}"
            )



    # --------------------------------------------------
    # Deterministic internal information detection
    # --------------------------------------------------

    for pattern in INTERNAL_PATTERNS:

        if pattern in message_lower:

            logfire.warning(
                "Deterministic internal information pattern matched: {pattern}",
                pattern=pattern
            )

            return GuardrailResult(
                status=GuardrailStatus.BLOCKED,
                response=(
                    "I can't provide private internal processes or reasoning. "
                    "I can help with Fonepay-related questions."
                ),
                reason=f"Deterministic internal information match: {pattern}"
            )



    with logfire.span("🛡️ Guardrails Check") as span:

        start = time.perf_counter()


        try:
            
            result = _rails.generate(
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                options={
                    "log": {
                        "activated_rails": True
                    }
                }
            )

            print("========== NEMO RAW RESULT ==========")
            print(result)
            print("=====================================")

            content = _extract_content(result)

            content_lower = content.lower()


            latency_ms = (
                time.perf_counter() - start
            ) * 1000



            # --------------------------------------------------
            # NeMo internal failure
            # --------------------------------------------------

            if NEMO_INTERNAL_ERROR_STRING in content_lower:

                _set_span_attrs(
                    span,
                    GuardrailStatus.ERROR.value,
                    message,
                    latency_ms,
                    content=content
                )

                return GuardrailResult(
                    status=GuardrailStatus.ERROR,
                    response=content,
                    reason="NeMo internal runtime error"
                )



            # --------------------------------------------------
            # Inspect activated rails
            # --------------------------------------------------

            rail_status, flow_name = _check_rail_fired(result)



            if rail_status == "blocked":

                logfire.info(
                    "Blocked rail detected: {flow}",
                    flow=flow_name
                )

                _set_span_attrs(
                    span,
                    GuardrailStatus.BLOCKED.value,
                    message,
                    latency_ms,
                    content=content,
                    flow_name=flow_name
                )


                return GuardrailResult(
                    status=GuardrailStatus.BLOCKED,
                    response=content,
                    reason=f"Rail triggered: {flow_name}"
                )



            if rail_status == "dialog":

                logfire.info(
                    "Dialog rail detected: {flow}",
                    flow=flow_name
                )


                _set_span_attrs(
                    span,
                    GuardrailStatus.DIALOG.value,
                    message,
                    latency_ms,
                    content=content,
                    flow_name=flow_name
                )


                return GuardrailResult(
                    status=GuardrailStatus.DIALOG,
                    response=content,
                    reason=f"Dialog rail triggered: {flow_name}"
                )



            # --------------------------------------------------
            # Normal RAG request
            # --------------------------------------------------

            _set_span_attrs(
                span,
                GuardrailStatus.PASS.value,
                message,
                latency_ms
            )


            return GuardrailResult(
                status=GuardrailStatus.PASS
            )



        except Exception as e:

            latency_ms = (
                time.perf_counter() - start
            ) * 1000


            _set_span_attrs(
                span,
                GuardrailStatus.ERROR.value,
                message,
                latency_ms,
                error=str(e)
            )

            print(repr(e))

            logfire.error(
                "❌ Guardrail execution exception: {error}",
                error=str(e)
            )


            return GuardrailResult(
                status=GuardrailStatus.ERROR,
                reason=f"Exception: {str(e)}"
            )