from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_event_item_request_builder import WithEvent_ItemRequestBuilder

class EventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}/events
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}/events", path_parameters)
    
    def by_event_id(self,event_id: str) -> WithEvent_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.webhooks.v1.projects.item.endpoints.item.events.item collection
        param event_id: The event_id path parameter.
        Returns: WithEvent_ItemRequestBuilder
        """
        if event_id is None:
            raise TypeError("event_id cannot be null.")
        from .item.with_event_item_request_builder import WithEvent_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event_id"] = event_id
        return WithEvent_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

