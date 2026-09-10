"""
Local embeddings via the Ollama OpenAI-compatible endpoint. No external APIs.

Default model: qwen3-embedding:0.6b. The vector dimension is probed at runtime
so switching models needs no config change (just re-ingest).
"""
import logfire
from langchain_openai import OpenAIEmbeddings
from app.config import settings

BATCH_SIZE = 64

_model = None
_dim: int | None = None


def _init():
    global _model
    if _model is not None:
        return
    logfire.info(f"Embeddings via Ollama: {settings.EMBEDDING_MODEL}")
    _model = OpenAIEmbeddings(
        base_url=f"{settings.OLLAMA_BASE_URL}/v1",
        api_key="local",
        model=settings.EMBEDDING_MODEL,
        check_embedding_ctx_length=False,  # don't tokenize with tiktoken
    )


def get_embedding_dim() -> int:
    global _dim
    if _dim is None:
        _init()
        _dim = len(_model.embed_query("dimension probe"))
        logfire.info(f"Embedding dimension: {_dim}")
    return _dim


def embed_query(query: str) -> list[float]:
    _init()
    with logfire.span("Query Embedding") as span:
        vec = _model.embed_query(query)
        if span:
            span.set_attribute("embedding.model", settings.EMBEDDING_MODEL)
            span.set_attribute("embedding.dimensions", len(vec))
    return vec


def embed_texts(texts: list[str]) -> list[list[float]]:
    _init()
    out: list[list[float]] = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        with logfire.span("Embed batch", model=settings.EMBEDDING_MODEL, start=i, size=len(batch)):
            out.extend(_model.embed_documents(batch))
    return out
