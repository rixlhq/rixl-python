from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .broadcast.broadcast_request_builder import BroadcastRequestBuilder
    from .subscribe.subscribe_request_builder import SubscribeRequestBuilder
    from .subscription.subscription_request_builder import SubscriptionRequestBuilder
    from .unsubscribe.unsubscribe_request_builder import UnsubscribeRequestBuilder

class BlogRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/blog
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BlogRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/blog", path_parameters)
    
    @property
    def broadcast(self) -> BroadcastRequestBuilder:
        """
        The broadcast property
        """
        from .broadcast.broadcast_request_builder import BroadcastRequestBuilder

        return BroadcastRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribe(self) -> SubscribeRequestBuilder:
        """
        The subscribe property
        """
        from .subscribe.subscribe_request_builder import SubscribeRequestBuilder

        return SubscribeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscription(self) -> SubscriptionRequestBuilder:
        """
        The subscription property
        """
        from .subscription.subscription_request_builder import SubscriptionRequestBuilder

        return SubscriptionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsubscribe(self) -> UnsubscribeRequestBuilder:
        """
        The unsubscribe property
        """
        from .unsubscribe.unsubscribe_request_builder import UnsubscribeRequestBuilder

        return UnsubscribeRequestBuilder(self.request_adapter, self.path_parameters)
    

