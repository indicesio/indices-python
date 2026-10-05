# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .no_proxy import NoProxy
from .datacenter_proxy import DatacenterProxy
from .residential_proxy import ResidentialProxy

__all__ = ["ProxySettings"]

ProxySettings: TypeAlias = Annotated[
    Union[DatacenterProxy, ResidentialProxy, NoProxy], PropertyInfo(discriminator="type")
]
