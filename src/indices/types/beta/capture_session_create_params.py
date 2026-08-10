# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .session_cookie_param import SessionCookieParam

__all__ = ["CaptureSessionCreateParams"]


class CaptureSessionCreateParams(TypedDict, total=False):
    cookies: Iterable[SessionCookieParam]
    """Initial cookies to set in the browser session."""

    use_proxy: bool
    """If true, spawn the browser session using a proxy."""
