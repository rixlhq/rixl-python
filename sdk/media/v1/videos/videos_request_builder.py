from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_video_item_request_builder import WithVideoItemRequestBuilder

class VideosRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/videos
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VideosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/videos", path_parameters)
    
    def by_video_id(self,video_id: str) -> WithVideoItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.v1.videos.item collection
        param video_id: Video ID
        Returns: WithVideoItemRequestBuilder
        """
        if video_id is None:
            raise TypeError("video_id cannot be null.")
        from .item.with_video_item_request_builder import WithVideoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["videoId"] = video_id
        return WithVideoItemRequestBuilder(self.request_adapter, url_tpl_params)
    

