# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SecretSlotDefinition"]


class SecretSlotDefinition(BaseModel):
    name: str
    """Name of the secret slot.

    Use this name as the identifier when binding secrets to a slot.
    """

    type: Literal["login", "string"]
    """Type of secret required: 'login' or 'string'."""

    supports_totp: Optional[bool] = None
    """
    Whether the connector can perform 2FA/TOTP when the bound login has it
    configured. Logins without TOTP remain bindable. Only applicable for 'login'
    type.
    """
