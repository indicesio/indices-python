# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Run", "Error"]


class Error(BaseModel):
    """Why the run failed.

    Present iff `status` is `connector_error`; for platform failures the status itself is the reason.
    """

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


class Run(BaseModel):
    id: str
    """Unique identifier for the object."""

    arguments: Dict[str, object]
    """Arguments in this run for the connector's input parameters."""

    connector_id: str
    """ID of the connector executed in this run."""

    created_at: datetime
    """Timestamp when the object was created."""

    error: Optional[Error] = None
    """Why the run failed.

    Present iff `status` is `connector_error`; for platform failures the status
    itself is the reason.
    """

    finished_at: Optional[datetime] = None
    """Timestamp when the object was last updated."""

    has_logs: bool
    """Whether the run has associated logs"""

    result_json: Optional[str] = None
    """Execution result of the run.

    In JSON, matching the connector's output schema. Limited to 100MB; results above
    100MB will be truncated and result in a `result_too_large` status.
    """

    status: Literal[
        "pending", "running", "success", "connector_error", "timed_out", "result_too_large", "internal_error"
    ]
    """
    Lifecycle status of the run: `pending`, `running`, `success`, `connector_error`,
    `timed_out`, `result_too_large`, or `internal_error`. `connector_error` means
    the connector's code failed (see `error`); `timed_out` and `internal_error` are
    platform outcomes worth retrying; `result_too_large` is not retryable as-is.
    """

    secret_bindings: Optional[Dict[str, str]] = None
    """Secrets to use for this run.

    This dict must be a mapping of secret slot names to secret IDs.
    """
