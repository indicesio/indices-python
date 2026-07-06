# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["TaskCreation", "Secret"]


class Secret(BaseModel):
    """A secret provided during task creation"""

    secret_id: str
    """ID of the secret to bind."""

    description: Optional[str] = None
    """
    Optional description of what this secret is used for (helps generate meaningful
    slot names).
    """


class TaskCreation(BaseModel):
    """Creation-related task data."""

    secret_bindings: Optional[Dict[str, str]] = None
    """Mapping of required secret slot names to secret IDs bound during task creation."""

    secrets: Optional[List[Secret]] = None
    """List of secrets provided during task creation."""
