# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FileFinalizeResponse"]


class FileFinalizeResponse(BaseModel):
    content_type: str
    """MIME type of the stored file."""

    crc32c: str
    """Base64-encoded CRC32C checksum reported by storage."""

    file_id: str
    """ID of the finalized file."""

    name: str
    """User-facing filename."""

    size_bytes: int
    """Size of the stored file in bytes, as reported by storage."""
