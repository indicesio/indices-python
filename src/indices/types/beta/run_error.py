# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["RunError"]


class RunError(BaseModel):
    details: Optional[Dict[str, object]] = None
    """Structured context reported by the connector."""

    exception: Optional[str] = None
    """Exception class name, when the failure came from a raised exception."""

    message: str
    """Human-readable description of the failure."""

    retryable: Optional[bool] = None
    """Whether retrying the run with the same arguments is expected to succeed.

    Null when unknown.
    """

    type: str
    """
    Machine-readable failure type: `auth_required`, `invalid_input`,
    `site_unavailable`, `site_changed`, `internal_error`, `crash`, or `unhandled`.
    """
