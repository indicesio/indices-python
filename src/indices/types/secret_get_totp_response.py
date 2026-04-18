# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SecretGetTotpResponse"]


class SecretGetTotpResponse(BaseModel):
    id: str
    """Unique identifier of the secret."""

    code: str
    """Current 6-digit TOTP code."""
