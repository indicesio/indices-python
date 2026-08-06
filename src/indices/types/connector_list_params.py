# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectorListParams"]


class ConnectorListParams(TypedDict, total=False):
    cursor: str
    """Cursor from a previous response's `next_cursor`, to fetch the next page."""

    limit: int
    """Maximum number of connectors to return."""
