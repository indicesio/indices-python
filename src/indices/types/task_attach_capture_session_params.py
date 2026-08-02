# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TaskAttachCaptureSessionParams"]


class TaskAttachCaptureSessionParams(TypedDict, total=False):
    capture_session_id: Required[str]
    """ID of a completed capture session to use as this task's recording.

    Attaching kicks off API generation from it.
    """
