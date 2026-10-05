# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DatacenterProxy"]


class DatacenterProxy(BaseModel):
    location: Literal["us", "eu"]

    type: Optional[Literal["datacenter"]] = None
