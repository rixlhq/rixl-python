from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.widgets_item_request_builder import WidgetsItemRequestBuilder

class WidgetsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /analytics/v1/dashboards/widgets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WidgetsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/analytics/v1/dashboards/widgets", path_parameters)
    
    def by_id(self,id: str) -> WidgetsItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.analytics.v1.dashboards.widgets.item collection
        param id: Unique identifier of the item
        Returns: WidgetsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.widgets_item_request_builder import WidgetsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return WidgetsItemRequestBuilder(self.request_adapter, url_tpl_params)
    

