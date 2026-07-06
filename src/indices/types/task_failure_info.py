# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TaskFailureInfo"]


class TaskFailureInfo(BaseModel):
    """Information about why a task failed, for user display."""

    category: str
    """Primary failure category"""

    message: str
    """Summary of the failure cause"""
