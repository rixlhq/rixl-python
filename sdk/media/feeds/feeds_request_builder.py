from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.github_com_rixlhq_api_internal_errors.error_response import ErrorResponse
    from ...models.github_com_rixlhq_api_internal_feeds_types.create_feed_request import CreateFeedRequest
    from ...models.github_com_rixlhq_api_internal_feeds_types.feed_response import FeedResponse
    from ...models.pagination.paginated_response_github_com_rixlhq_api_internal_feeds_types_feed_response import PaginatedResponseGithub_com_rixlhq_api_internal_feeds_types_FeedResponse
    from .feeds_get_request_body import FeedsGetRequestBody
    from .item.with_feed_item_request_builder import WithFeedItemRequestBuilder

class FeedsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/feeds
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FeedsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/feeds{?limit*,offset*}", path_parameters)
    
    def by_feed_id(self,feed_id: str) -> WithFeedItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.feeds.item collection
        param feed_id: Feed ID
        Returns: WithFeedItemRequestBuilder
        """
        if feed_id is None:
            raise TypeError("feed_id cannot be null.")
        from .item.with_feed_item_request_builder import WithFeedItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["feedId"] = feed_id
        return WithFeedItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,body: FeedsGetRequestBody, request_configuration: Optional[RequestConfiguration[FeedsRequestBuilderGetQueryParameters]] = None) -> Optional[PaginatedResponseGithub_com_rixlhq_api_internal_feeds_types_FeedResponse]:
        """
        Lists all feeds for the active project with pagination.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PaginatedResponseGithub_com_rixlhq_api_internal_feeds_types_FeedResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_get_request_information(
            body, request_configuration
        )
        from ...models.github_com_rixlhq_api_internal_errors.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "401": ErrorResponse,
            "403": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.pagination.paginated_response_github_com_rixlhq_api_internal_feeds_types_feed_response import PaginatedResponseGithub_com_rixlhq_api_internal_feeds_types_FeedResponse

        return await self.request_adapter.send_async(request_info, PaginatedResponseGithub_com_rixlhq_api_internal_feeds_types_FeedResponse, error_mapping)
    
    async def post(self,body: CreateFeedRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FeedResponse]:
        """
        Creates a new feed under the active project.
        param body: Feed details
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FeedResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.github_com_rixlhq_api_internal_errors.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "401": ErrorResponse,
            "403": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.github_com_rixlhq_api_internal_feeds_types.feed_response import FeedResponse

        return await self.request_adapter.send_async(request_info, FeedResponse, error_mapping)
    
    def to_get_request_information(self,body: FeedsGetRequestBody, request_configuration: Optional[RequestConfiguration[FeedsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists all feeds for the active project with pagination.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_post_request_information(self,body: CreateFeedRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new feed under the active project.
        param body: Feed details
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> FeedsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FeedsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FeedsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FeedsRequestBuilderGetQueryParameters():
        """
        Lists all feeds for the active project with pagination.
        """
        # Limit
        limit: Optional[int] = None

        # Offset
        offset: Optional[int] = None

    
    @dataclass
    class FeedsRequestBuilderGetRequestConfiguration(RequestConfiguration[FeedsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FeedsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

