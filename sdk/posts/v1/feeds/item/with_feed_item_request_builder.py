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
    from .....models.postsv1.list_posts_response import ListPostsResponse
    from .creators.creators_request_builder import CreatorsRequestBuilder
    from .item.with_post_item_request_builder import WithPostItemRequestBuilder

class WithFeedItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /posts/v1/feeds/{feedId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithFeedItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/posts/v1/feeds/{feedId}{?limit*,offset*}", path_parameters)
    
    def by_post_id(self,post_id: str) -> WithPostItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.posts.v1.feeds.item.item collection
        param post_id: Post ID
        Returns: WithPostItemRequestBuilder
        """
        if post_id is None:
            raise TypeError("post_id cannot be null.")
        from .item.with_post_item_request_builder import WithPostItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["postId"] = post_id
        return WithPostItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithFeedItemRequestBuilderGetQueryParameters]] = None) -> Optional[ListPostsResponse]:
        """
        Public, unauthenticated listing of posts in a feed, with pagination.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListPostsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.postsv1.list_posts_response import ListPostsResponse

        return await self.request_adapter.send_async(request_info, ListPostsResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithFeedItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Public, unauthenticated listing of posts in a feed, with pagination.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithFeedItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithFeedItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithFeedItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def creators(self) -> CreatorsRequestBuilder:
        """
        The creators property
        """
        from .creators.creators_request_builder import CreatorsRequestBuilder

        return CreatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithFeedItemRequestBuilderGetQueryParameters():
        """
        Public, unauthenticated listing of posts in a feed, with pagination.
        """
        # Page size
        limit: Optional[int] = None

        # Page offset
        offset: Optional[int] = None

    
    @dataclass
    class WithFeedItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithFeedItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

