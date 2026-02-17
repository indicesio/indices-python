# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RunLogsResponse"]


class RunLogsResponse(BaseModel):
    stderr: str
    """Standard error output from the run execution."""

    stdout: str
    """Standard output from the run execution."""
