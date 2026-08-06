# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .secret_slot_definition import SecretSlotDefinition

__all__ = ["Connector"]


class Connector(BaseModel):
    id: str
    """Unique identifier for the object."""

    created_at: datetime
    """Timestamp when the object was created."""

    display_name: str
    """Short human-readable name of the connector."""

    input_schema: Dict[str, object]
    """JSON Schema for the connector's run arguments."""

    output_schema: Dict[str, object]
    """JSON Schema for the connector's run results."""

    purpose: str
    """What the connector does, as specified at publish time."""

    revised_from_connector_id: Optional[str] = None
    """Connector this one revised (if any)."""

    task_id: Optional[str] = None
    """Task this connector was generated from; null for directly published connectors."""

    website: Optional[str] = None
    """Website the connector operates against."""

    required_secrets: Optional[List[SecretSlotDefinition]] = None
    """Secret slots that must be bound when running the connector."""
