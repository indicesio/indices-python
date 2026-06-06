# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RunLogsResponse"]


class RunLogsResponse(BaseModel):
    logs: str
    """Run execution logs."""
