# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileCreateResponse"]


class FileCreateResponse(BaseModel):
    expires_at: datetime
    """When the upload URL stops being valid."""

    file_id: str
    """Server-assigned ID of the pending file."""

    upload_headers: Dict[str, str]
    """
    Headers that must be sent verbatim with the PUT; they are covered by the URL
    signature.
    """

    upload_url: str
    """Signed URL the sandbox must PUT the file bytes to."""
