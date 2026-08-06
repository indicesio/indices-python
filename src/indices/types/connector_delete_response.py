# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectorDeleteResponse"]


class ConnectorDeleteResponse(BaseModel):
    id: str
    """Unique identifier for the deleted connector."""

    deleted: bool
    """Whether the connector was deleted."""
