# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """Unique identifier for the object."""

    content_type: str
    """MIME type of the file."""

    crc32c: str
    """Base64-encoded CRC32C checksum of the file content."""

    created_at: datetime
    """Timestamp when the file was created."""

    name: str
    """User-facing filename."""

    run_id: str
    """ID of the run that produced this file."""

    size_bytes: int
    """Size of the file in bytes."""
