# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TaskCreateParams", "CreationParams", "CreationParamsSecret"]


class TaskCreateParams(TypedDict, total=False):
    creation_params: Required[CreationParams]
    """Information used during task creation."""

    display_name: Required[str]
    """Short title shown in the dashboard.

    Informational only; not used to generate the task.
    """

    task: Required[str]
    """Detailed explanation of the task to be performed."""


class CreationParamsSecret(TypedDict, total=False):
    """A secret provided during task creation"""

    secret_id: Required[str]
    """ID of the secret to bind."""

    description: Optional[str]
    """
    Optional description of what this secret is used for (helps generate meaningful
    slot names).
    """


class CreationParams(TypedDict, total=False):
    """Information used during task creation."""

    secrets: Iterable[CreationParamsSecret]
    """List of secrets to use for this task."""
