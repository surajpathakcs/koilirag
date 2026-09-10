"""
Local, API-free guardrails.

1. Deterministic regex for jailbreak / prompt-injection / internal-info probes.
2. Embedding-similarity intent router (greeting / farewell / capabilities /
   off-topic) using the same local embedding model as retrieval.

No LLM call, no NeMo. When nothing matches with confidence, the message PASSes
through to the RAG graph, whose grounding prompt handles the rest.
"""
import re
import time
import logfire
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import Optional

from app.services.retrieval.embedding import embed_query, embed_texts


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


# ── Deterministic blocking patterns ────────────────────────────────────────────

_JAILBREAK_RE = re.compile(
    r"\b(ignore (all |your )?previous instructions|ignore your instructions|"
    r"forget your (instructions|system prompt|rules)|forget you are|stop being|"
    r"disregard (all |your )?(previous )?instructions|reveal your (system )?prompt|"
    r"show (me )?your (system |hidden )?(prompt|instructions)|what('| i)?s your prompt|"
    r"act as (dan|an unrestricted|a different)|developer mode|jailbreak|"
    r"you are now (an? |unrestricted|chatgpt)|pretend you (are|have no)|"
    r"bypass your (restrictions|rules|safety)|override your rules)\b",
    re.IGNORECASE,
)

_INTERNAL_RE = re.compile(
    r"\b(show (me )?your (reasoning|chain of thought|thought process|analysis|"
    r"agent steps|graph steps|retrieval steps)|what (tools|model) (did you use|are you)|"
    r"how (do you retrieve|were you built|does your system work internally)|"
    r"explain your (architecture|internal process|system))\b",
    re.IGNORECASE,
)

_BLOCK_JAILBREAK_MSG = (
    "I can't provide internal instructions or system details. "
    "I can help with Koili TMS questions."
)
_BLOCK_INTERNAL_MSG = (
    "I can't provide private internal processes or reasoning. "
    "I can help with Koili TMS questions."
)

# ── Dialog / off-topic intent phrases ─────────────────────────────────────────

_CAPABILITIES_MSG = (
    "I'm the Koili TMS Assistant. I can answer questions about using the Koili "
    "Terminal Management System — logging in and user roles, the dashboard, "
    "branches, users, merchants, IPN devices, schemes, partners, billing, "
    "settings, audit logs, and profile management."
)
_GREETING_MSG = (
    "Hello! I'm the Koili TMS Assistant. I can help with using the Koili "
    "Terminal Management System — branches, users and roles, merchants, IPN "
    "devices, schemes, partners, billing, settings, and audit logs. How can I help?"
)
_FAREWELL_MSG = "Goodbye! Feel free to return if you have more questions about Koili TMS."
_OFFTOPIC_MSG = (
    "I'm the Koili TMS Assistant. I can only help with using the Koili Terminal "
    "Management System. I can't help with unrelated topics."
)

_INTENTS = {
    "greeting": {
        "response": _GREETING_MSG,
        "status": GuardrailStatus.DIALOG,
        "threshold": 0.72,
        "phrases": [
            "hello", "hi", "hey there", "good morning", "good afternoon",
            "namaste", "hi how are you", "greetings",
        ],
    },
    "farewell": {
        "response": _FAREWELL_MSG,
        "status": GuardrailStatus.DIALOG,
        "threshold": 0.72,
        "phrases": [
            "bye", "goodbye", "see you later", "thanks bye", "that is all",
            "thank you goodbye",
        ],
    },
    "capabilities": {
        "response": _CAPABILITIES_MSG,
        "status": GuardrailStatus.DIALOG,
        "threshold": 0.66,
        "phrases": [
            "what can you do", "what do you know", "what are you",
            "what topics do you cover", "what can i ask you", "help",
            "who are you", "what is this assistant",
        ],
    },
    "off_topic": {
        "response": _OFFTOPIC_MSG,
        "status": GuardrailStatus.BLOCKED,
        "threshold": 0.62,
        "phrases": [
            "tell me a joke", "write me a poem", "what is the capital of france",
            "what is the weather today", "recommend a movie", "write a python script",
            "help me with my homework", "solve my math problem", "give me a recipe",
            "who won the football match", "translate this sentence to french",
            "what is the meaning of life",
        ],
    },
}

_intent_vectors: dict[str, np.ndarray] = {}


def initialize_rails() -> None:
    """Precompute intent phrase embeddings once at startup."""
    global _intent_vectors
    for name, cfg in _INTENTS.items():
        vecs = np.array(embed_texts(cfg["phrases"]), dtype=np.float32)
        vecs /= np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-8
        _intent_vectors[name] = vecs
    logfire.info(f"🛡️ Local guardrails initialised ({len(_intent_vectors)} intents).")


def _best_similarity(query_vec: np.ndarray, mat: np.ndarray) -> float:
    return float(np.max(mat @ query_vec))


def guard(message: str) -> GuardrailResult:
    text = (message or "").strip()
    if not text:
        return GuardrailResult(GuardrailStatus.PASS)

    with logfire.span("🛡️ Guardrails Check") as span:
        start = time.perf_counter()

        if _JAILBREAK_RE.search(text):
            return GuardrailResult(
                GuardrailStatus.BLOCKED, _BLOCK_JAILBREAK_MSG, "jailbreak pattern"
            )
        if _INTERNAL_RE.search(text):
            return GuardrailResult(
                GuardrailStatus.BLOCKED, _BLOCK_INTERNAL_MSG, "internal-info pattern"
            )

        if not _intent_vectors:
            return GuardrailResult(GuardrailStatus.PASS)

        qv = np.array(embed_query(text), dtype=np.float32)
        qv /= np.linalg.norm(qv) + 1e-8

        scores = {n: _best_similarity(qv, m) for n, m in _intent_vectors.items()}
        best = max(scores, key=scores.get)
        best_score = scores[best]

        if span:
            span.set_attribute("guardrail.intent", best)
            span.set_attribute("guardrail.score", round(best_score, 3))
            span.set_attribute("guardrail.latency_ms", round((time.perf_counter() - start) * 1000, 1))

        if best_score >= _INTENTS[best]["threshold"]:
            cfg = _INTENTS[best]
            return GuardrailResult(cfg["status"], cfg["response"], f"intent: {best} ({best_score:.2f})")

        return GuardrailResult(GuardrailStatus.PASS)
