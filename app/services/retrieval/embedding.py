"""
Local embeddings via fastembed (ONNX, CPU). No external APIs.

Default model: BAAI/bge-base-en-v1.5 (768-dim). Query and passage embeddings
use fastembed's asymmetric helpers when available so bge's retrieval
instruction is applied to queries only.
"""
import logfire
from app.config import settings

BATCH_SIZE = 64

_model = None


def _init():
    global _model
    if _model is not None:
        return
    from fastembed import TextEmbedding

    logfire.info(f"Loading fastembed model: {settings.EMBEDDING_MODEL}")
    _model = TextEmbedding(model_name=settings.EMBEDDING_MODEL)


def get_embedding_dim() -> int:
    return settings.EMBEDDING_DIM


def embed_query(query: str) -> list[float]:
    _init()
    with logfire.span("🔢 Query Embedding") as span:
        try:
            vec = next(iter(_model.query_embed(query)))
        except AttributeError:
            vec = next(iter(_model.embed([query])))
        if span:
            span.set_attribute("embedding.model", settings.EMBEDDING_MODEL)
            span.set_attribute("embedding.dimensions", len(vec))
    return vec.tolist()


def embed_texts(texts: list[str]) -> list[list[float]]:
    _init()
    out: list[list[float]] = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        with logfire.span("Embed batch", model=settings.EMBEDDING_MODEL, start=i, size=len(batch)):
            out.extend(v.tolist() for v in _model.embed(batch))
    return out
