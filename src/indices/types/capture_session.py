# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .capture_session_state import CaptureSessionState

__all__ = ["CaptureSession"]


class CaptureSession(BaseModel):
    id: str
    """Unique identifier for the capture session."""

    browser_session_id: Optional[str] = None
    """Opaque identifier for the spawned browser session.

    Null once the browser is gone.
    """

    created_at: datetime
    """Timestamp when the object was created."""

    iframe_url: Optional[str] = None
    """URL to embed in an iframe to control the browser.

    Only usable while the session is active.
    """

    state: CaptureSessionState
    """Current state of the capture session.

    A session records while active, is completing once completion is requested, and
    becomes a reusable recording once completed.
    """

    updated_at: datetime
    """Timestamp when the object was last updated."""
