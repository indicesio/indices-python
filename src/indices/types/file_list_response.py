# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from .._models import BaseModel

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
    data: List[File]
    """Files for the requested page, ordered newest first."""

    has_more: bool
    """Whether more files exist after this page."""

    next_cursor: Optional[str] = None
    """Pass as the `cursor` query parameter to fetch the next page.

    Null when has_more is false.
    """
