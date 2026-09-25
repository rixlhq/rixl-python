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
    from ......models.feeds.v1.feed import Feed
    from ......models.feeds.v1.list_feeds_response import ListFeedsResponse
    from .feeds_post_request_body import FeedsPostRequestBody
    from .item.with_feed_item_request_builder import WithFeed_ItemRequestBuilder

class FeedsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /feeds/v1/projects/{project_id}/feeds
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FeedsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/feeds/v1/projects/{project_id}/feeds{?pagination%2Elimit*,pagination%2Eoffset*}", path_parameters)
    
    def by_feed_id(self,feed_id: str) -> WithFeed_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.feeds.v1.projects.item.feeds.item collection
        param feed_id: Unique identifier of the item
        Returns: WithFeed_ItemRequestBuilder
        """
        if feed_id is None:
            raise TypeError("feed_id cannot be null.")
        from .item.with_feed_item_request_builder import WithFeed_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["feed_id"] = feed_id
        return WithFeed_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FeedsRequestBuilderGetQueryParameters]] = None) -> Optional[ListFeedsResponse]:
        """
        ListFeeds
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListFeedsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.feeds.v1.list_feeds_response import ListFeedsResponse

        return await self.request_adapter.send_async(request_info, ListFeedsResponse, None)
    
    async def post(self,body: FeedsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Feed]:
        """
        CreateFeed
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Feed]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.feeds.v1.feed import Feed

        return await self.request_adapter.send_async(request_info, Feed, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FeedsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListFeeds
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: FeedsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        CreateFeed
        param body: The request body
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
        ListFeeds
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "pagination_limit":
                return "pagination%2Elimit"
            if original_name == "pagination_offset":
                return "pagination%2Eoffset"
            return original_name
        
        # Maximum number of items to return.
        pagination_limit: Optional[int] = None

        # Number of items to skip before collecting the result set.
        pagination_offset: Optional[int] = None

    
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
    

