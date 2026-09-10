"""
Local LLM gateway. Talks to an OpenAI-compatible endpoint (Ollama by default,
also works with llama.cpp --api or vLLM). No external APIs.
"""
from langchain_openai import ChatOpenAI

from app.config import settings

# Model per capability. "rag" is the main answer model; planner/grader/query
# rewriting use the (optionally smaller) fast model.
_MODEL_BY_FEATURE = {
    "rag": settings.LLM_MODEL,
    "grader": settings.LLM_MODEL_FAST,
    "planner": settings.LLM_MODEL_FAST,
    "query_rewriter": settings.LLM_MODEL_FAST,
}


def get_langchain_llm(feature: str = "rag"):
    """Return a LangChain chat model pointed at the local inference server."""
    if feature not in _MODEL_BY_FEATURE:
        raise ValueError(f"Unknown LLM feature: {feature}")

    return ChatOpenAI(
        base_url=f"{settings.OLLAMA_BASE_URL}/v1",
        api_key="local",  # ignored by Ollama, required by the client
        model=_MODEL_BY_FEATURE[feature],
        temperature=0,
        timeout=settings.LLM_TIMEOUT,
        max_retries=1,
    )


def extract_cache_status(response) -> str:  # kept for API compatibility
    return "MISS"
