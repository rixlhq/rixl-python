from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .replay.replay_request_builder import ReplayRequestBuilder

class WithEvent_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}/events/{event_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithEvent_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}/events/{event_id}", path_parameters)
    
    @property
    def replay(self) -> ReplayRequestBuilder:
        """
        The replay property
        """
        from .replay.replay_request_builder import ReplayRequestBuilder

        return ReplayRequestBuilder(self.request_adapter, self.path_parameters)
    

