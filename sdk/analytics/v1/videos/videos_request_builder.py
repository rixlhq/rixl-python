from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_video_item_request_builder import WithVideo_ItemRequestBuilder

class VideosRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /analytics/v1/videos
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VideosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/analytics/v1/videos", path_parameters)
    
    def by_video_id(self,video_id: str) -> WithVideo_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.analytics.v1.videos.item collection
        param video_id: Unique identifier of the item
        Returns: WithVideo_ItemRequestBuilder
        """
        if video_id is None:
            raise TypeError("video_id cannot be null.")
        from .item.with_video_item_request_builder import WithVideo_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["video_id"] = video_id
        return WithVideo_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

