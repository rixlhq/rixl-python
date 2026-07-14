from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_image_item_request_builder import WithImage_ItemRequestBuilder

class ImagesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/images
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ImagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/images", path_parameters)
    
    def by_image_id(self,image_id: str) -> WithImage_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.v1.images.item collection
        param image_id: Unique identifier of the item
        Returns: WithImage_ItemRequestBuilder
        """
        if image_id is None:
            raise TypeError("image_id cannot be null.")
        from .item.with_image_item_request_builder import WithImage_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["image_id"] = image_id
        return WithImage_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

