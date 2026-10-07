# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .datacenter_proxy_param import DatacenterProxyParam
from .residential_proxy_param import ResidentialProxyParam

__all__ = [
    "RunCreateParams",
    "ProxySettings",
    "SecretValues",
    "SecretValuesLoginSecretValue",
    "SecretValuesStringSecretValue",
]


class RunCreateParams(TypedDict, total=False):
    connector_id: Required[str]
    """ID of the connector to execute."""

    arguments: Dict[str, object]
    """Arguments to pass to the connector.

    Optional if the connector does not require any arguments.
    """

    async_: Annotated[bool, PropertyInfo(alias="async")]
    """
    When true, return immediately with a pending run; poll retrieveRun for the
    result. Results above 1,000,000 UTF-8 JSON bytes are discarded and finish with
    result_too_large. Retry those requests with async=false to receive the result
    directly.
    """

    max_timeout_s: int
    """Maximum execution time in seconds before the run is timed out."""

    proxy_settings: Optional[ProxySettings]
    """Proxy for the network traffic of this run.

    If you do not set it, a setting is automatically determined by the platform.
    """

    secret_bindings: Dict[str, str]
    """Mapping of secret slot names to the IDs of saved, user-owned secrets.

    Each of the connector's required_secrets must appear here or in secret_values,
    but not both.
    """

    secret_values: Dict[str, SecretValues]
    """
    Mapping of secret slot names to secret values supplied directly for this run,
    instead of referencing a saved secret. Use a login shape ({username, password,
    totp_secret?}) for login slots and a string shape ({value}) for string slots.
    Values are not persisted.
    """


ProxySettings: TypeAlias = Union[DatacenterProxyParam, ResidentialProxyParam]


class SecretValuesLoginSecretValue(TypedDict, total=False):
    password: Required[str]
    """Password for the login."""

    username: Required[str]
    """Username for the login."""

    totp_secret: Optional[str]
    """TOTP seed, when the login uses 2FA."""


class SecretValuesStringSecretValue(TypedDict, total=False):
    value: Required[str]
    """The secret value."""


SecretValues: TypeAlias = Union[SecretValuesLoginSecretValue, SecretValuesStringSecretValue]
