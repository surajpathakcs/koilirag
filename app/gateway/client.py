import logfire
from portkey_ai import Portkey, createHeaders, PORTKEY_GATEWAY_URL
from langchain_openai import ChatOpenAI

from app.config import settings


from langchain_groq import ChatGroq

# Production gateway config (used only when PORTKEY_CONFIG_ID is NOT set in .env):
#   Strategy: loadbalance across primary and fallback Groq key (both llama-3.3-70b)
#   Cache: simple mode — identical prompts reuse cached responses
#   Retry: 2 attempts on 429/503 before switching target
active_config = settings.PORTKEY_CONFIG_ID if settings.PORTKEY_CONFIG_ID else {
    "strategy": {"mode": "loadbalance"},
    "cache": {"mode": "simple"},
    "retry": {
        "attempts": 2,
        "on_status_codes": [429, 503]
    },
    "targets": [
        {"weight": 0.5, "override_params": {"model": f"@{settings.GROQ_SLUG}/llama-3.3-70b-versatile"}},
        {"weight": 0.5, "override_params": {"model": f"@{settings.GROQ_SLUG_FALLBACK}/llama-3.3-70b-versatile"}},
    ]
}

if settings.PORTKEY_API_KEY:
    portkey_client = Portkey(
        api_key=settings.PORTKEY_API_KEY,
        config=active_config
    )
else:
    portkey_client = None


def get_langchain_llm(feature: str = "rag"):
    """
    Returns a Portkey-backed ChatOpenAI model if Portkey is configured,
    or falls back cleanly to direct ChatGroq if Portkey is not configured or blocked.
    """
    if settings.PORTKEY_API_KEY and settings.PORTKEY_CONFIG_ID:
        return ChatOpenAI(
            api_key=settings.PORTKEY_API_KEY,
            base_url=PORTKEY_GATEWAY_URL,
            model=f"@{settings.GROQ_SLUG}/llama-3.3-70b-versatile",
            temperature=0,
            default_headers=createHeaders(
                api_key=settings.PORTKEY_API_KEY,
                config=settings.PORTKEY_CONFIG_ID,
                metadata={
                    "feature": feature,
                    "_user": "rag-system",
                    "environment": "production"
                }
            )
        )
    
    # Fallback to direct ChatGroq if Portkey is not configured.
    # Prefers the fallback key if available (separate daily quota from primary).
    groq_key = settings.GROQ_API_KEY_FALLBACK or settings.GROQ_API_KEY
    groq_model = settings.GROQ_MODEL_NAME_FALLBACK or settings.GROQ_MODEL_NAME
    logfire.info(f"Using direct ChatGroq LLM for feature: {feature} (model: {groq_model})")
    return ChatGroq(
        api_key=groq_key,
        model=groq_model,
        temperature=0
    )

def extract_cache_status(response) -> str:
    """
    Pull x-portkey-cache-status from the Portkey native client response headers.
    Tries multiple attribute paths defensively — returns 'MISS' if not found.
    """
    for attr in ("_raw_response", "_response", "_http_response"):
        raw = getattr(response, attr, None)
        if raw is not None:
            status = getattr(raw, "headers", {}).get("x-portkey-cache-status", "")
            if status:
                return status.upper()
    return "MISS"