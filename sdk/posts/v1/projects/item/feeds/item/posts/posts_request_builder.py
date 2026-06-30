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
    from ........models.gateway.create_post_body import CreatePostBody
    from ........models.postsv1.list_posts_response import ListPostsResponse
    from ........models.postsv1.post import Post
    from .creators.creators_request_builder import CreatorsRequestBuilder
    from .item.with_post_item_request_builder import WithPostItemRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class PostsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /posts/v1/projects/{projectId}/feeds/{feedId}/posts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PostsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/posts/v1/projects/{projectId}/feeds/{feedId}/posts{?limit*,offset*}", path_parameters)
    
    def by_post_id(self,post_id: str) -> WithPostItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.posts.v1.projects.item.feeds.item.posts.item collection
        param post_id: Post ID
        Returns: WithPostItemRequestBuilder
        """
        if post_id is None:
            raise TypeError("post_id cannot be null.")
        from .item.with_post_item_request_builder import WithPostItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["postId"] = post_id
        return WithPostItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PostsRequestBuilderGetQueryParameters]] = None) -> Optional[ListPostsResponse]:
        """
        List posts in a feed
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListPostsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.postsv1.list_posts_response import ListPostsResponse

        return await self.request_adapter.send_async(request_info, ListPostsResponse, None)
    
    async def post(self,body: CreatePostBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Post]:
        """
        Create a new post in a feed
        param body: Post to create
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Post]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.postsv1.post import Post

        return await self.request_adapter.send_async(request_info, Post, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PostsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        List posts in a feed
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreatePostBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new post in a feed
        param body: Post to create
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
    
    def with_url(self,raw_url: str) -> PostsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PostsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PostsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def creators(self) -> CreatorsRequestBuilder:
        """
        The creators property
        """
        from .creators.creators_request_builder import CreatorsRequestBuilder

        return CreatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PostsRequestBuilderGetQueryParameters():
        """
        List posts in a feed
        """
        # Page size
        limit: Optional[int] = None

        # Page offset
        offset: Optional[int] = None

    
    @dataclass
    class PostsRequestBuilderGetRequestConfiguration(RequestConfiguration[PostsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PostsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

