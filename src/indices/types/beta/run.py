# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .run_error import RunError
from .proxy_settings import ProxySettings

__all__ = ["Run"]


class Run(BaseModel):
    id: str
    """Unique identifier for the object."""

    arguments: Dict[str, object]
    """Arguments in this run for the connector's input parameters."""

    connector_id: str
    """ID of the connector executed in this run."""

    connector_version: int
    """Version of the connector executed in this run.

    Runs pin the version that was newest when they were created.
    """

    created_at: datetime
    """Timestamp when the object was created."""

    error: Optional[RunError] = None
    """Why the run failed.

    Present iff `status` is `connector_error`; for platform failures the status
    itself is the reason.
    """

    finished_at: Optional[datetime] = None
    """Timestamp when the object was last updated."""

    has_logs: bool
    """Whether the run has associated logs"""

    proxy_settings: ProxySettings
    """Proxy that the run uses for its network traffic.

    This is the `proxy_settings` of the request. If the request did not set it, a
    setting is automatically determined by the platform.
    """

    result: Optional[Dict[str, object]] = None
    """Execution result of the run, matching the connector's output schema.

    Synchronous requests return successful results up to the 100 MB execution limit.
    Only results of at most 1,000,000 UTF-8 JSON bytes are stored. Larger results
    are returned once to the synchronous caller and are null on later retrieval. If
    delivery fails, the result cannot be retrieved later.
    """

    result_size_bytes: Optional[int] = None
    """Size of the executor's serialized result in UTF-8 bytes, when known."""

    result_stored: bool
    """Whether the result is retained for later retrieval."""

    status: Literal[
        "pending", "running", "success", "connector_error", "timed_out", "result_too_large", "internal_error"
    ]
    """
    Lifecycle status of the run: `pending`, `running`, `success`, `connector_error`,
    `timed_out`, `result_too_large`, or `internal_error`. `connector_error` means
    the connector's code failed (see `error`); `timed_out` and `internal_error` are
    platform outcomes worth retrying; `result_too_large` means the result exceeded
    the execution limit or could not be retained for an async caller. Async results
    above 1 MB require a new synchronous request.
    """

    secret_bindings: Optional[Dict[str, str]] = None
    """Secrets to use for this run.

    This dict must be a mapping of secret slot names to secret IDs.
    """
