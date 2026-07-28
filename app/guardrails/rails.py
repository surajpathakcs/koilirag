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
    ERROR = "error"


@dataclass
class GuardrailResult:
    status: GuardrailStatus
    response: Optional[str] = None
    reason: Optional[str] = None


# Known NeMo internal failure string — returned as content, not as an exception
NEMO_INTERNAL_ERROR_STRING = "an internal error has occurred"

# Colang flow names that represent a safety block.
# These are matched against NeMo's activated_rails log, NOT against raw text.
_BLOCK_FLOW_NAMES = {"handle off topic", "jailbreak protection"}

# Colang flow names for dialog rails (greeting, farewell, capabilities).
# These are handled directly by the guardrail and never reach the RAG pipeline.
_DIALOG_FLOW_NAMES = {"greeting", "farewell", "capabilities"}


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
      - Without options  → dict  {'role': 'assistant', 'content': '...'}
      - With options     → GenerationResponse (Pydantic model)
    This helper normalises both cases to a plain string.
    """
    if hasattr(result, "response"):
        # GenerationResponse — .response is a list of message dicts
        resp = result.response
        if isinstance(resp, list) and resp:
            return resp[0].get("content", "")
        return str(resp)
    if isinstance(result, dict):
        return result.get("content", "")
    return str(result)


def _check_rail_fired(result) -> tuple[bool, Optional[str]]:
    """
    Inspect the NeMo activated_rails log to determine whether a safety or
    dialog rail fired.  Returns (fired: bool, flow_name: str | None).
    """
    if not hasattr(result, "log") or result.log is None:
        return False, None

    activated = result.log.activated_rails or []
    for rail in activated:
        name = rail.name.lower()
        if name in _BLOCK_FLOW_NAMES or name in _DIALOG_FLOW_NAMES:
            return True, rail.name
    return False, None


def _set_span_attrs(span, status: str, message: str, latency_ms: float,
                    content: Optional[str] = None, error: Optional[str] = None,
                    flow_name: Optional[str] = None) -> None:
    """Centralised span attribute writer — avoids repeating the same 5 lines."""
    if not span:
        return
    span.set_attribute("guardrail.status", status)
    span.set_attribute("guardrail.query_length", len(message))
    span.set_attribute("guardrail.latency_ms", round(latency_ms, 1))
    if content:
        span.set_attribute("guardrail.response_snippet", content[:100])
    if error:
        span.set_attribute("guardrail.error", error[:200])
    if flow_name:
        span.set_attribute("guardrail.flow_name", flow_name)


# ── Guard Function ──────────────────────────────────────────────────────────────

def guard(message: str) -> GuardrailResult:
    """
    Run a user message through the NeMo safety gate.

    Returns a GuardrailResult with one of three explicit statuses:
      PASS    — query is clean, proceed to RAG pipeline.
      BLOCKED — a safety rail fired, return the guardrail response immediately.
      ERROR   — NeMo engine failed internally, caller decides fail-open/closed.
    """
    if _rails is None:
        logfire.warning("⚠️ Guardrails not initialised — cannot evaluate safety.")
        return GuardrailResult(
            status=GuardrailStatus.ERROR,
            reason="Guardrails engine not initialised"
        )

    with logfire.span("🛡️ Guardrails Check") as span:
        start = time.perf_counter()
        try:
            # Request the activated_rails log so we can inspect which
            # Colang flow fired rather than guessing from response text.
            result = _rails.generate(
                messages=[{"role": "user", "content": message}],
                options={"log": {"activated_rails": True}}
            )

            content = _extract_content(result)
            content_lower = content.lower()
            latency_ms = (time.perf_counter() - start) * 1000

            # ── 1. Detect NeMo internal engine failure ──────────────────────
            if NEMO_INTERNAL_ERROR_STRING in content_lower:
                _set_span_attrs(span, GuardrailStatus.ERROR.value,
                                message, latency_ms, content=content)
                logfire.error("❌ NeMo engine returned internal error instead of a decision.")
                return GuardrailResult(
                    status=GuardrailStatus.ERROR,
                    reason="NeMo internal runtime error",
                    response=content
                )

            # ── 2. Check if a safety or dialog rail fired ───────────────────
            fired, flow_name = _check_rail_fired(result)

            if fired:
                _set_span_attrs(span, GuardrailStatus.BLOCKED.value,
                                message, latency_ms, content=content,
                                flow_name=flow_name)
                return GuardrailResult(
                    status=GuardrailStatus.BLOCKED,
                    response=content,
                    reason=f"Rail triggered: {flow_name}"
                )

            # ── 3. Clean pass ───────────────────────────────────────────────
            _set_span_attrs(span, GuardrailStatus.PASS.value,
                            message, latency_ms)
            return GuardrailResult(status=GuardrailStatus.PASS)

        except Exception as e:
            latency_ms = (time.perf_counter() - start) * 1000
            _set_span_attrs(span, GuardrailStatus.ERROR.value,
                            message, latency_ms, error=str(e))
            logfire.error("❌ Guardrail execution exception: {error}", error=str(e))
            return GuardrailResult(
                status=GuardrailStatus.ERROR,
                reason=f"Exception: {str(e)}"
            )
