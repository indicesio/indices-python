# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .connectors import (
    ConnectorsResource,
    AsyncConnectorsResource,
    ConnectorsResourceWithRawResponse,
    AsyncConnectorsResourceWithRawResponse,
    ConnectorsResourceWithStreamingResponse,
    AsyncConnectorsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .capture_sessions import (
    CaptureSessionsResource,
    AsyncCaptureSessionsResource,
    CaptureSessionsResourceWithRawResponse,
    AsyncCaptureSessionsResourceWithRawResponse,
    CaptureSessionsResourceWithStreamingResponse,
    AsyncCaptureSessionsResourceWithStreamingResponse,
)

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def connectors(self) -> ConnectorsResource:
        """Manage connectors."""
        return ConnectorsResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        """Execute a connector."""
        return RunsResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        """Manage secrets like login credentials and API keys."""
        return SecretsResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def capture_sessions(self) -> CaptureSessionsResource:
        """
        Record a browser session; a completed capture is a reusable input for building connectors.
        """
        return CaptureSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/indicesio/indices-python#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/indicesio/indices-python#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        """Manage connectors."""
        return AsyncConnectorsResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        """Execute a connector."""
        return AsyncRunsResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        """Manage secrets like login credentials and API keys."""
        return AsyncSecretsResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def capture_sessions(self) -> AsyncCaptureSessionsResource:
        """
        Record a browser session; a completed capture is a reusable input for building connectors.
        """
        return AsyncCaptureSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/indicesio/indices-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/indicesio/indices-python#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def connectors(self) -> ConnectorsResourceWithRawResponse:
        """Manage connectors."""
        return ConnectorsResourceWithRawResponse(self._beta.connectors)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        """Execute a connector."""
        return RunsResourceWithRawResponse(self._beta.runs)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        """Manage secrets like login credentials and API keys."""
        return SecretsResourceWithRawResponse(self._beta.secrets)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._beta.files)

    @cached_property
    def capture_sessions(self) -> CaptureSessionsResourceWithRawResponse:
        """
        Record a browser session; a completed capture is a reusable input for building connectors.
        """
        return CaptureSessionsResourceWithRawResponse(self._beta.capture_sessions)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithRawResponse:
        """Manage connectors."""
        return AsyncConnectorsResourceWithRawResponse(self._beta.connectors)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        """Execute a connector."""
        return AsyncRunsResourceWithRawResponse(self._beta.runs)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        """Manage secrets like login credentials and API keys."""
        return AsyncSecretsResourceWithRawResponse(self._beta.secrets)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._beta.files)

    @cached_property
    def capture_sessions(self) -> AsyncCaptureSessionsResourceWithRawResponse:
        """
        Record a browser session; a completed capture is a reusable input for building connectors.
        """
        return AsyncCaptureSessionsResourceWithRawResponse(self._beta.capture_sessions)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def connectors(self) -> ConnectorsResourceWithStreamingResponse:
        """Manage connectors."""
        return ConnectorsResourceWithStreamingResponse(self._beta.connectors)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        """Execute a connector."""
        return RunsResourceWithStreamingResponse(self._beta.runs)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        """Manage secrets like login credentials and API keys."""
        return SecretsResourceWithStreamingResponse(self._beta.secrets)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._beta.files)

    @cached_property
    def capture_sessions(self) -> CaptureSessionsResourceWithStreamingResponse:
        """
        Record a browser session; a completed capture is a reusable input for building connectors.
        """
        return CaptureSessionsResourceWithStreamingResponse(self._beta.capture_sessions)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """Manage connectors."""
        return AsyncConnectorsResourceWithStreamingResponse(self._beta.connectors)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        """Execute a connector."""
        return AsyncRunsResourceWithStreamingResponse(self._beta.runs)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        """Manage secrets like login credentials and API keys."""
        return AsyncSecretsResourceWithStreamingResponse(self._beta.secrets)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._beta.files)

    @cached_property
    def capture_sessions(self) -> AsyncCaptureSessionsResourceWithStreamingResponse:
        """
        Record a browser session; a completed capture is a reusable input for building connectors.
        """
        return AsyncCaptureSessionsResourceWithStreamingResponse(self._beta.capture_sessions)
