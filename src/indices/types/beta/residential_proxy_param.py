# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResidentialProxyParam"]


class ResidentialProxyParam(TypedDict, total=False):
    location: Required[Literal["us"]]

    type: Literal["residential"]
