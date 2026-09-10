"""Shared Qdrant client (one per process).

Embedded mode (local directory) by default — no server, no port. Set QDRANT_URL
to use a remote/containerised Qdrant instead.

Embedded Qdrant is single-process: the directory can be opened by only one
client at a time. This module hands out a single shared instance so multiple
modules in the same process don't collide. Do not run ingestion while the API
process is up — stop one before starting the other. For concurrent access, run
Qdrant as a server and set QDRANT_URL.
"""
from qdrant_client import QdrantClient
from app.config import settings

_client: QdrantClient | None = None


def get_qdrant_client() -> QdrantClient:
    global _client
    if _client is None:
        if settings.QDRANT_URL:
            _client = QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY or None)
        else:
            _client = QdrantClient(path=settings.QDRANT_PATH)
    return _client
