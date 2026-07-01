# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .run import Run
from .._models import BaseModel

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    data: List[Run]
    """Runs for the requested page, ordered newest first."""

    has_more: bool
    """Whether more runs exist after this page."""

    next_cursor: Optional[str] = None
    """Pass as the `cursor` query parameter to fetch the next page.

    Null when has_more is false.
    """
