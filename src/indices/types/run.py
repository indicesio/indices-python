# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Run"]


class Run(BaseModel):
    id: str
    """Unique identifier for the object."""

    arguments: Dict[str, object]
    """Arguments in this run for the task's input parameters."""

    connector_id: str
    """ID of the connector executed in this run."""

    created_at: datetime
    """Timestamp when the object was created."""

    finished_at: Optional[datetime] = None
    """Timestamp when the object was last updated."""

    has_logs: bool
    """Whether the run has associated logs"""

    result_json: Optional[str] = None
    """Execution result of the run.

    In JSON, matching the task's output schema. Limited to 100MB; results above
    100MB will be truncated and result in a `result_too_large` status.
    """

    status: Literal["pending", "running", "success", "failed", "timed_out", "result_too_large", "internal_error"]
    """
    Lifecycle status of the run: `pending`, `running`, `success`, `failed`,
    `timed_out`, `result_too_large`, or `internal_error`.
    """

    task_id: Optional[str] = None
    """ID of the task executed in this run; null for direct connector runs."""

    secret_bindings: Optional[Dict[str, str]] = None
    """Secrets to use for this run.

    This dict must be a mapping of secret slot names to secret IDs.
    """
