from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.billingv1.create_subscription_response import CreateSubscriptionResponse
    from ....models.billingv1.subscription import Subscription
    from ....models.gateway.create_subscription_body import CreateSubscriptionBody
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .history.history_request_builder import HistoryRequestBuilder
    from .reactivate.reactivate_request_builder import ReactivateRequestBuilder
    from .upgrade.upgrade_request_builder import UpgradeRequestBuilder

class SubscriptionRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /billing/v1/subscription
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SubscriptionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/billing/v1/subscription", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Subscription]:
        """
        Returns the current organization subscription.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Subscription]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.billingv1.subscription import Subscription

        return await self.request_adapter.send_async(request_info, Subscription, None)
    
    async def post(self,body: CreateSubscriptionBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CreateSubscriptionResponse]:
        """
        Create a subscription for the authenticated organization
        param body: Subscription request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreateSubscriptionResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.billingv1.create_subscription_response import CreateSubscriptionResponse

        return await self.request_adapter.send_async(request_info, CreateSubscriptionResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the current organization subscription.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateSubscriptionBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a subscription for the authenticated organization
        param body: Subscription request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> SubscriptionRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SubscriptionRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SubscriptionRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        The cancel property
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def history(self) -> HistoryRequestBuilder:
        """
        The history property
        """
        from .history.history_request_builder import HistoryRequestBuilder

        return HistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reactivate(self) -> ReactivateRequestBuilder:
        """
        The reactivate property
        """
        from .reactivate.reactivate_request_builder import ReactivateRequestBuilder

        return ReactivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upgrade(self) -> UpgradeRequestBuilder:
        """
        The upgrade property
        """
        from .upgrade.upgrade_request_builder import UpgradeRequestBuilder

        return UpgradeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SubscriptionRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SubscriptionRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

