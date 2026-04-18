# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SecretDeleteResponse"]


class SecretDeleteResponse(BaseModel):
    id: str
    """Unique identifier of the deleted secret."""

    deleted: bool
    """Whether the secret was successfully deleted."""
