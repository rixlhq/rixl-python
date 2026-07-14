from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_creator_item_request_builder import WithCreator_ItemRequestBuilder

class CreatorsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /posts/v1/feeds/{feed_id}/creators
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CreatorsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/posts/v1/feeds/{feed_id}/creators", path_parameters)
    
    def by_creator_id(self,creator_id: str) -> WithCreator_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.posts.v1.feeds.item.creators.item collection
        param creator_id: Unique identifier of the item
        Returns: WithCreator_ItemRequestBuilder
        """
        if creator_id is None:
            raise TypeError("creator_id cannot be null.")
        from .item.with_creator_item_request_builder import WithCreator_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["creator_id"] = creator_id
        return WithCreator_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

