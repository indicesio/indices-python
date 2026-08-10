# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SecretSlotDefinition"]


class SecretSlotDefinition(BaseModel):
    name: str
    """Name of the secret slot, used as the key in a run's secret_bindings."""

    type: Literal["login", "string"]
    """Type of secret required: 'login' or 'string'."""

    description: Optional[str] = None
    """What the bound secret is used for, when the connector declares it."""

    supports_totp: Optional[bool] = None
    """
    Whether the connector can perform 2FA/TOTP when the bound login has it
    configured. Logins without TOTP remain bindable. Only applicable for 'login'
    type.
    """
