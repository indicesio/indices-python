# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    task_id: Required[str]
    """The ID of the task to list runs for."""

    cursor: Optional[str]
    """Cursor from a previous response's `next_cursor`, to fetch the next page."""

    limit: int
    """Maximum number of runs to return."""
