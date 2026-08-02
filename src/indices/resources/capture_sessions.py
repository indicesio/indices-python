# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import capture_session_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.capture_session import CaptureSession
from ..types.session_cookie_param import SessionCookieParam
from ..types.capture_session_list_response import CaptureSessionListResponse

__all__ = ["CaptureSessionsResource", "AsyncCaptureSessionsResource"]


class CaptureSessionsResource(SyncAPIResource):
    """
    Record a browser session; a completed capture is a reusable input for task generation.
    """

    @cached_property
    def with_raw_response(self) -> CaptureSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/indicesio/indices-python#accessing-raw-response-data-eg-headers
        """
        return CaptureSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CaptureSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/indicesio/indices-python#with_streaming_response
        """
        return CaptureSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cookies: Iterable[SessionCookieParam] | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSession:
        """
        <p>Spawn a browser session that records the network traffic of everything done in it.</p><p>Once completed, the capture session is a reusable recording: attach it to a task to generate an API from it.</p>

        Args:
          cookies: Initial cookies to set in the browser session.

          use_proxy: If true, spawn the browser session using a proxy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1beta/capture_sessions",
            body=maybe_transform(
                {
                    "cookies": cookies,
                    "use_proxy": use_proxy,
                },
                capture_session_create_params.CaptureSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSession,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSession:
        """
        <p>Retrieve a capture session by its ID.</p><p>Poll this after requesting completion: the session is a usable recording once <code>state</code> is <code>completed</code>.</p>

        Args:
          id: The ID of the capture session to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1beta/capture_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSession,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSessionListResponse:
        """<p>List all capture sessions, newest first.</p>"""
        return self._get(
            "/v1beta/capture_sessions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSessionListResponse,
        )

    def complete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSession:
        """
        <p>Stop recording and finalize the capture session.</p><p>Completion is asynchronous: the browser uploads its recording and the session then transitions to <code>completed</code>. Poll <code>retrieveCaptureSession</code> to observe the transition.</p>

        Args:
          id: The ID of the capture session to complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1beta/capture_sessions/{id}/complete", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSession,
        )


class AsyncCaptureSessionsResource(AsyncAPIResource):
    """
    Record a browser session; a completed capture is a reusable input for task generation.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCaptureSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/indicesio/indices-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCaptureSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCaptureSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/indicesio/indices-python#with_streaming_response
        """
        return AsyncCaptureSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cookies: Iterable[SessionCookieParam] | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSession:
        """
        <p>Spawn a browser session that records the network traffic of everything done in it.</p><p>Once completed, the capture session is a reusable recording: attach it to a task to generate an API from it.</p>

        Args:
          cookies: Initial cookies to set in the browser session.

          use_proxy: If true, spawn the browser session using a proxy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1beta/capture_sessions",
            body=await async_maybe_transform(
                {
                    "cookies": cookies,
                    "use_proxy": use_proxy,
                },
                capture_session_create_params.CaptureSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSession,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSession:
        """
        <p>Retrieve a capture session by its ID.</p><p>Poll this after requesting completion: the session is a usable recording once <code>state</code> is <code>completed</code>.</p>

        Args:
          id: The ID of the capture session to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1beta/capture_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSession,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSessionListResponse:
        """<p>List all capture sessions, newest first.</p>"""
        return await self._get(
            "/v1beta/capture_sessions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSessionListResponse,
        )

    async def complete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSession:
        """
        <p>Stop recording and finalize the capture session.</p><p>Completion is asynchronous: the browser uploads its recording and the session then transitions to <code>completed</code>. Poll <code>retrieveCaptureSession</code> to observe the transition.</p>

        Args:
          id: The ID of the capture session to complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1beta/capture_sessions/{id}/complete", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureSession,
        )


class CaptureSessionsResourceWithRawResponse:
    def __init__(self, capture_sessions: CaptureSessionsResource) -> None:
        self._capture_sessions = capture_sessions

        self.create = to_raw_response_wrapper(
            capture_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            capture_sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            capture_sessions.list,
        )
        self.complete = to_raw_response_wrapper(
            capture_sessions.complete,
        )


class AsyncCaptureSessionsResourceWithRawResponse:
    def __init__(self, capture_sessions: AsyncCaptureSessionsResource) -> None:
        self._capture_sessions = capture_sessions

        self.create = async_to_raw_response_wrapper(
            capture_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            capture_sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            capture_sessions.list,
        )
        self.complete = async_to_raw_response_wrapper(
            capture_sessions.complete,
        )


class CaptureSessionsResourceWithStreamingResponse:
    def __init__(self, capture_sessions: CaptureSessionsResource) -> None:
        self._capture_sessions = capture_sessions

        self.create = to_streamed_response_wrapper(
            capture_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            capture_sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            capture_sessions.list,
        )
        self.complete = to_streamed_response_wrapper(
            capture_sessions.complete,
        )


class AsyncCaptureSessionsResourceWithStreamingResponse:
    def __init__(self, capture_sessions: AsyncCaptureSessionsResource) -> None:
        self._capture_sessions = capture_sessions

        self.create = async_to_streamed_response_wrapper(
            capture_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            capture_sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            capture_sessions.list,
        )
        self.complete = async_to_streamed_response_wrapper(
            capture_sessions.complete,
        )
