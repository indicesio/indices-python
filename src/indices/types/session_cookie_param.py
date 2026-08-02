# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionCookieParam"]


class SessionCookieParam(TypedDict, total=False):
    """A cookie to set in the browser session."""

    name: Required[str]
    """The name of the cookie."""

    value: Required[str]
    """The value of the cookie."""

    domain: Optional[str]
    """The domain of the cookie."""

    http_only: Optional[bool]
    """Whether the cookie is HTTP only."""

    path: Optional[str]
    """The path of the cookie."""

    secure: Optional[bool]
    """Whether the cookie is secure."""
