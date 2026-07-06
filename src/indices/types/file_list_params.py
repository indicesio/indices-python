# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    run_id: Required[str]
    """The ID of the run whose files to list."""

    cursor: Optional[str]
    """Cursor from a previous response's `next_cursor`, to fetch the next page."""

    limit: int
    """Maximum number of files to return."""
