# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    cursor: str
    """Cursor from a previous response's `next_cursor`, to fetch the next page."""

    filename: str
    """Only files whose name contains this text."""

    limit: int
    """Maximum number of files to return."""

    order: Literal["asc", "desc"]
    """Sort direction."""

    run_id: str
    """Only files produced by this run."""

    sort: Literal["name", "created_at", "size_bytes", "source"]
    """Column to sort by: name, created_at, size_bytes, or source."""

    source: Literal["UPLOAD", "RUN_OUTPUT", "GENERATION", "FORGE_SESSION"]
    """Only files from this source."""

    task_id: str
    """Only files produced by runs of this task."""
