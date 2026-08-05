# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

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

    run_id: Optional[str] = None
    """ID of the run that produced this file. Null for uploaded files."""

    size_bytes: int
    """Size of the file in bytes."""

    source: Literal["UPLOAD", "RUN_OUTPUT", "GENERATION", "FORGE_SESSION"]
    """How the file came to exist: uploaded by the user or produced by a run."""

    task_id: Optional[str] = None
    """ID of the task whose run produced this file. Null for uploaded files."""
