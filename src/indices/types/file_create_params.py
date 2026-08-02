# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    content_type: Required[str]
    """MIME type of the file content."""

    name: Required[str]
    """User-facing filename, e.g. 'report.pdf'."""

    size_bytes: Required[int]
    """Exact size of the file in bytes. Enforced by the signed upload URL."""
