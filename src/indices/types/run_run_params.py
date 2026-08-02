# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunRunParams"]


class RunRunParams(TypedDict, total=False):
    connector_id: Required[str]
    """ID of the connector to execute."""

    arguments: Dict[str, object]
    """Arguments to pass to the connector.

    Optional if the connector does not require any arguments.
    """

    async_: Annotated[bool, PropertyInfo(alias="async")]
    """
    When true, return immediately with a pending run; poll retrieveRun for the
    result.
    """

    max_timeout_s: int
    """Maximum execution time in seconds before the run is timed out."""

    secret_bindings: Dict[str, str]
    """Mapping of secret slot names to secret IDs.

    Each slot defined in the connector's required_secrets must be mapped to a
    user-owned secret.
    """
