# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import connector_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.connector import Connector
from ..types.connector_delete_response import ConnectorDeleteResponse
from ..types.connector_list_revisions_response import ConnectorListRevisionsResponse

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    """Manage connectors."""

    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/indicesio/indices-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/indicesio/indices-python#with_streaming_response
        """
        return ConnectorsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        <p>Retrieve a connector by its ID.</p>

        Args:
          connector_id: The ID of the connector to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            path_template("/v1beta/connectors/{connector_id}", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Connector]:
        """
        <p>List the connectors in your catalog.</p>

        Args:
          cursor: Cursor from a previous response's `next_cursor`, to fetch the next page.

          limit: Maximum number of connectors to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1beta/connectors",
            page=SyncCursorPage[Connector],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=Connector,
        )

    def delete(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorDeleteResponse:
        """
        <p>Delete a connector by its ID.</p><p>A legacy task that generated the connector is kept, but is detached and no longer runnable.</p>

        Args:
          connector_id: The ID of the connector to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._delete(
            path_template("/v1beta/connectors/{connector_id}", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorDeleteResponse,
        )

    def list_revisions(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListRevisionsResponse:
        """
        <p>List the full revision lineage of a connector, newest first.</p>

        Args:
          connector_id: The ID of the connector whose revisions to list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            path_template("/v1beta/connectors/{connector_id}/revisions", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorListRevisionsResponse,
        )


class AsyncConnectorsResource(AsyncAPIResource):
    """Manage connectors."""

    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/indicesio/indices-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/indicesio/indices-python#with_streaming_response
        """
        return AsyncConnectorsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        <p>Retrieve a connector by its ID.</p>

        Args:
          connector_id: The ID of the connector to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            path_template("/v1beta/connectors/{connector_id}", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Connector, AsyncCursorPage[Connector]]:
        """
        <p>List the connectors in your catalog.</p>

        Args:
          cursor: Cursor from a previous response's `next_cursor`, to fetch the next page.

          limit: Maximum number of connectors to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1beta/connectors",
            page=AsyncCursorPage[Connector],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=Connector,
        )

    async def delete(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorDeleteResponse:
        """
        <p>Delete a connector by its ID.</p><p>A legacy task that generated the connector is kept, but is detached and no longer runnable.</p>

        Args:
          connector_id: The ID of the connector to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._delete(
            path_template("/v1beta/connectors/{connector_id}", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorDeleteResponse,
        )

    async def list_revisions(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListRevisionsResponse:
        """
        <p>List the full revision lineage of a connector, newest first.</p>

        Args:
          connector_id: The ID of the connector whose revisions to list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            path_template("/v1beta/connectors/{connector_id}/revisions", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorListRevisionsResponse,
        )


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = to_raw_response_wrapper(
            connectors.retrieve,
        )
        self.list = to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = to_raw_response_wrapper(
            connectors.delete,
        )
        self.list_revisions = to_raw_response_wrapper(
            connectors.list_revisions,
        )


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = async_to_raw_response_wrapper(
            connectors.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connectors.delete,
        )
        self.list_revisions = async_to_raw_response_wrapper(
            connectors.list_revisions,
        )


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = to_streamed_response_wrapper(
            connectors.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = to_streamed_response_wrapper(
            connectors.delete,
        )
        self.list_revisions = to_streamed_response_wrapper(
            connectors.list_revisions,
        )


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.retrieve = async_to_streamed_response_wrapper(
            connectors.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connectors.delete,
        )
        self.list_revisions = async_to_streamed_response_wrapper(
            connectors.list_revisions,
        )
