"""
Screenshot fetching from this project's own MinIO (S3-compatible) bucket.

The API exposes GET /images/{name} which streams the object, so MinIO stays
private and the UI only ever talks to the API.
"""
import re
import mimetypes
import logfire
from app.config import settings

_client = None

# Only allow the manual's own screenshot filenames.
_NAME_RE = re.compile(r"^manual_img_\d{1,4}\.(png|jpe?g)$", re.IGNORECASE)


def _get_client():
    global _client
    if _client is None:
        from minio import Minio

        _client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE,
        )
    return _client


def is_valid_name(name: str) -> bool:
    return bool(_NAME_RE.match(name or ""))


def fetch_image(name: str) -> tuple[bytes, str]:
    """Return (bytes, content_type). Raises on missing object."""
    client = _get_client()
    resp = None
    try:
        resp = client.get_object(settings.MINIO_BUCKET, name)
        data = resp.read()
    finally:
        if resp is not None:
            resp.close()
            resp.release_conn()
    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    logfire.debug("Served image {name} ({size} bytes)", name=name, size=len(data))
    return data, content_type
