from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .feeds.feeds_request_builder import FeedsRequestBuilder
    from .posts.posts_request_builder import PostsRequestBuilder

class WithProject_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /posts/v1/projects/{project_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProject_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/posts/v1/projects/{project_id}", path_parameters)
    
    @property
    def feeds(self) -> FeedsRequestBuilder:
        """
        The feeds property
        """
        from .feeds.feeds_request_builder import FeedsRequestBuilder

        return FeedsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def posts(self) -> PostsRequestBuilder:
        """
        The posts property
        """
        from .posts.posts_request_builder import PostsRequestBuilder

        return PostsRequestBuilder(self.request_adapter, self.path_parameters)
    

