# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .connector import Connector

__all__ = ["ConnectorListRevisionsResponse"]


class ConnectorListRevisionsResponse(BaseModel):
    data: List[Connector]
    """The connector's full revision history, most recent first.

    The first entry is the current revision.
    """
