# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
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

    website: Required[str]
    """The website to perform the task on."""

    input_schema: Optional[str]
    """Task input parameters as a JSON schema string.

    Required when auto_generate_schemas is disabled. When auto_generate_schemas is
    enabled, this may be omitted and remains null until generation completes.
    """

    output_schema: Optional[str]
    """Task output schema as a JSON schema string.

    Required when auto_generate_schemas is disabled. When auto_generate_schemas is
    enabled, this may be omitted and remains null until generation completes.
    """


class CreationParamsSecret(TypedDict, total=False):
    """A secret provided during task creation"""

    secret_uuid: Required[str]
    """UUID of the secret to bind."""

    description: Optional[str]
    """
    Optional description of what this secret is used for (helps generate meaningful
    slot names).
    """


class CreationParams(TypedDict, total=False):
    """Information used during task creation."""

    auto_generate_schemas: bool
    """
    If true, input and output schemas will be automatically generated from captured
    HAR traffic. When enabled, input_schema and output_schema in the request are
    optional. If omitted, task responses may return null for these fields until
    generation completes.
    """

    initial_input_values: Dict[str, object]
    """Initial values for input schema fields, keyed by property name.

    Used during task creation to demonstrate the task. Especially important for
    tasks requiring authentication, as initial credentials must be provided.
    """

    is_fully_autonomous: bool
    """If true, the server will run the browser task autonomously.

    If false, the user must complete the task manually in a spawned browser.
    """

    secrets: Iterable[CreationParamsSecret]
    """List of secrets to use for this task."""
