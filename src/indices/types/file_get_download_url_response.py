# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["FileGetDownloadURLResponse"]


class FileGetDownloadURLResponse(BaseModel):
    expires_at: datetime
    """When the download URL stops being valid."""

    url: str
    """Short-lived signed URL to download the file bytes directly from storage."""
