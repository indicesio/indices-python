# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .task_creation import TaskCreation
from .task_failure_info import TaskFailureInfo
from .secret_slot_definition import SecretSlotDefinition

__all__ = ["Task"]


class Task(BaseModel):
    id: str
    """Unique identifier for the object."""

    connector_id: Optional[str] = None
    """The connector executed when this task is run; pass it to the runs endpoints.

    Null until the task is ready. Changes when a revision publishes a new connector.
    """

    created_at: datetime
    """Timestamp when the object was created."""

    creation: TaskCreation
    """Parameters set during the creation of this task."""

    current_state: Literal["not_ready", "waiting_for_manual_completion", "ready", "failed"]
    """Current state of the task, in particular whether it is ready to use."""

    display_name: str
    """Short title shown in the dashboard. Informational only."""

    input_schema: Optional[Dict[str, object]] = None
    """Task input schema as a JSON Schema object.

    May be null while the task is not ready (e.g. schema generation in progress).
    Guaranteed non-null when current_state is ready.
    """

    output_schema: Optional[Dict[str, object]] = None
    """Task output schema as a JSON Schema object.

    May be null while the task is not ready (e.g. schema generation in progress).
    Guaranteed non-null when current_state is ready.
    """

    task: str
    """Detailed explanation of the task to be performed."""

    updated_at: datetime
    """Timestamp when the object was last updated."""

    website: Optional[str] = None
    """The primary URL the task targets.

    May be null while the task is not ready; non-null once generation completes.
    """

    failure_info: Optional[TaskFailureInfo] = None
    """Information about why a task failed, for user display."""

    required_secrets: Optional[List[SecretSlotDefinition]] = None
    """List of secrets that must be provided when running this task."""
