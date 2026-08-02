# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SecretSlotDefinition"]


class SecretSlotDefinition(BaseModel):
    """Definition of a secret slot that a connector requires."""

    name: str
    """
    Name of the secret slot (used as env var prefix, e.g., 'LOGIN' →
    LOGIN_USERNAME).
    """

    type: Literal["login", "string"]
    """Type of secret required: 'login' or 'string'."""

    requires_totp: Optional[bool] = None
    """Whether this login slot requires 2FA/TOTP. Only applicable for 'login' type."""
