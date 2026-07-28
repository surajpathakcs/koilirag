from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL
from langchain_openai import ChatOpenAI

from app.config import settings


# Portkey routing configuration.
#
# Flow:
# Primary Groq Virtual Key
#        |
#        | failure / rate limit
#        v
# Secondary Groq Virtual Key
#        |
#        | failure / rate limit
#        v
# Tertiary Groq Virtual Key
#
# In production, PORTKEY_CONFIG_ID should normally point
# to the configuration stored in Portkey dashboard.
#
# For local development, fallback configuration is used.

portkey_config = (
    settings.PORTKEY_CONFIG_ID
    if settings.PORTKEY_CONFIG_ID
    else {
        "strategy": {
            "mode": "fallback"
        },
        "retry": {
            "attempts": 3,
            "on_status_codes": [
                429,
                500,
                502,
                503,
                504
            ]
        },
        "cache": {
            "mode": "simple"
        },
        "targets": [
            {
                "virtual_key": settings.PORTKEY_GROQ_PRIMARY_SLUG
            },
            {
                "virtual_key": settings.PORTKEY_GROQ_SECONDARY_SLUG
            },
            {
                "virtual_key": settings.PORTKEY_GROQ_TERTIARY_SLUG
            }
        ]
    }
)


# Model selection by capability.
#
# RAG:
#   Main answer generation.
#   Uses a larger model.
#
# Grader:
#   Hallucination / faithfulness checking.
#   Uses a smaller faster model.
#
# Query rewriter:
#   Query optimization.
#   Uses a smaller faster model.

MODEL_CONFIGS = {
    "rag": {
        "model": "llama-3.3-70b-versatile"
    },

    "grader": {
        "model": "llama-3.3-70b-versatile"
    },

    "planner": {
        "model": "llama-3.3-70b-versatile"
    },

    "query_rewriter": {
        "model": "llama-3.3-70b-versatile"
    }
}


def get_langchain_llm(feature: str = "rag"):
    """
    Returns a Portkey-backed LangChain LLM.

    Supported features:
    - rag: main answer generation
    - grader: hallucination / faithfulness checking
    - query_rewriter: query optimization
    """

    if not settings.PORTKEY_API_KEY:
        raise RuntimeError(
            "PORTKEY_API_KEY is missing."
        )

    if feature not in MODEL_CONFIGS:
        raise ValueError(
            f"Unknown LLM feature: {feature}"
        )

    model_config = MODEL_CONFIGS[feature]

    return ChatOpenAI(
        api_key=settings.PORTKEY_API_KEY,
        base_url=PORTKEY_GATEWAY_URL,
        model=model_config["model"],
        temperature=0,
        default_headers=createHeaders(
            api_key=settings.PORTKEY_API_KEY,
            config=portkey_config,
            metadata={
                "feature": feature,
                "_user": "rag-system",
                "environment": settings.ENVIRONMENT
            }
        )
    )


def extract_cache_status(response) -> str:
    """
    Extract Portkey cache status from response headers.
    """

    for attr in (
        "_raw_response",
        "_response",
        "_http_response"
    ):
        raw = getattr(response, attr, None)

        if raw is not None:
            status = getattr(
                raw,
                "headers",
                {}
            ).get(
                "x-portkey-cache-status",
                ""
            )

            if status:
                return status.upper()

    return "MISS"