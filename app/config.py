import os
from dotenv import load_dotenv

load_dotenv()


def _flag(name: str, default: str = "false") -> bool:
    return (os.getenv(name) or default).strip().lower() in ("1", "true", "yes", "on")


class Settings:
    # ── LLM (local, OpenAI-compatible: Ollama / llama.cpp / vLLM) ──────────────
    LLM_PROVIDER: str = (os.getenv("LLM_PROVIDER") or "ollama").strip().lower()
    OLLAMA_BASE_URL: str = (os.getenv("OLLAMA_BASE_URL") or "http://localhost:11434").strip().rstrip("/")
    # Main answer-generation model.
    LLM_MODEL: str = (os.getenv("LLM_MODEL") or "qwen2.5:7b-instruct-q4_K_M").strip()
    # Smaller/faster model for planner + grader. Defaults to the main model.
    LLM_MODEL_FAST: str = (os.getenv("LLM_MODEL_FAST") or os.getenv("LLM_MODEL") or "qwen2.5:7b-instruct-q4_K_M").strip()
    LLM_TIMEOUT: int = int(os.getenv("LLM_TIMEOUT") or "120")

    # ── Embeddings (local, fastembed ONNX on CPU) ─────────────────────────────
    EMBEDDING_MODEL: str = (os.getenv("EMBEDDING_MODEL") or "BAAI/bge-base-en-v1.5").strip()
    EMBEDDING_DIM: int = int(os.getenv("EMBEDDING_DIM") or "768")

    # ── Vector store (embedded Qdrant — local directory, no server) ───────────
    QDRANT_PATH: str = (os.getenv("QDRANT_PATH") or "./qdrant_data").strip()
    # Optional remote Qdrant; only used when QDRANT_URL is set.
    QDRANT_URL: str = (os.getenv("QDRANT_URL") or "").strip()
    QDRANT_API_KEY: str = (os.getenv("QDRANT_API_KEY") or "").strip()
    QDRANT_COLLECTION: str = (os.getenv("QDRANT_COLLECTION_NAME") or "koili_tms_manual").strip()

    # ── Retrieval tuning ─────────────────────────────────────────────────────
    RETRIEVAL_CANDIDATES: int = int(os.getenv("RETRIEVAL_CANDIDATES") or "25")
    RETRIEVAL_TOP_N: int = int(os.getenv("RETRIEVAL_TOP_N") or "5")

    # ── Graph behaviour ─────────────────────────────────────────────────────
    ENABLE_GRADER: bool = _flag("ENABLE_GRADER", "true")

    ENVIRONMENT: str = (os.getenv("ENVIRONMENT") or "local").strip()


settings = Settings()
