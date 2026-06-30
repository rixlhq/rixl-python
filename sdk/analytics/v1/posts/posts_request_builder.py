from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_post_item_request_builder import WithPostItemRequestBuilder

class PostsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /analytics/v1/posts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PostsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/analytics/v1/posts", path_parameters)
    
    def by_post_id(self,post_id: str) -> WithPostItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.analytics.v1.posts.item collection
        param post_id: Post ID
        Returns: WithPostItemRequestBuilder
        """
        if post_id is None:
            raise TypeError("post_id cannot be null.")
        from .item.with_post_item_request_builder import WithPostItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["postId"] = post_id
        return WithPostItemRequestBuilder(self.request_adapter, url_tpl_params)
    

