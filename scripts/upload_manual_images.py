"""
Upload the manual's screenshots to this project's MinIO bucket.

    python -m scripts.upload_manual_images            # DATA/images
    python -m scripts.upload_manual_images path/to/dir

Only files named manual_img_*.png/.jpg/.jpeg are uploaded.
"""
import os
import re
import sys
import mimetypes

from minio import Minio
from app.config import settings

_NAME_RE = re.compile(r"^manual_img_\d{1,4}\.(png|jpe?g)$", re.IGNORECASE)


def main(src_dir: str = "DATA/images") -> None:
    client = Minio(
        settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=settings.MINIO_SECURE,
    )

    if not client.bucket_exists(settings.MINIO_BUCKET):
        client.make_bucket(settings.MINIO_BUCKET)
        print(f"Created bucket '{settings.MINIO_BUCKET}'.")

    names = sorted(f for f in os.listdir(src_dir) if _NAME_RE.match(f))
    if not names:
        print(f"No manual_img_* files in {src_dir}.")
        return

    for i, name in enumerate(names, 1):
        path = os.path.join(src_dir, name)
        ctype = mimetypes.guess_type(name)[0] or "application/octet-stream"
        client.fput_object(settings.MINIO_BUCKET, name, path, content_type=ctype)
        if i % 50 == 0 or i == len(names):
            print(f"  {i}/{len(names)}")

    print(f"Uploaded {len(names)} images to '{settings.MINIO_BUCKET}'.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "DATA/images")
