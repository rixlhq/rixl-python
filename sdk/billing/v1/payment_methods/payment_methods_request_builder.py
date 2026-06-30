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
    from ....models.billingv1.list_payment_methods_response import ListPaymentMethodsResponse
    from ....models.billingv1.payment_method_details import PaymentMethodDetails
    from ....models.gateway.upsert_payment_method_body import UpsertPaymentMethodBody
    from .from_payment_intent.from_payment_intent_request_builder import FromPaymentIntentRequestBuilder
    from .from_setup_intent.from_setup_intent_request_builder import FromSetupIntentRequestBuilder
    from .item.with_payment_method_item_request_builder import WithPaymentMethodItemRequestBuilder

class PaymentMethodsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /billing/v1/payment-methods
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PaymentMethodsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/billing/v1/payment-methods", path_parameters)
    
    def by_payment_method_id(self,payment_method_id: str) -> WithPaymentMethodItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.billing.v1.paymentMethods.item collection
        param payment_method_id: Payment method ID
        Returns: WithPaymentMethodItemRequestBuilder
        """
        if payment_method_id is None:
            raise TypeError("payment_method_id cannot be null.")
        from .item.with_payment_method_item_request_builder import WithPaymentMethodItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["paymentMethodId"] = payment_method_id
        return WithPaymentMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ListPaymentMethodsResponse]:
        """
        Returns the organization's payment methods.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListPaymentMethodsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.billingv1.list_payment_methods_response import ListPaymentMethodsResponse

        return await self.request_adapter.send_async(request_info, ListPaymentMethodsResponse, None)
    
    async def post(self,body: UpsertPaymentMethodBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PaymentMethodDetails]:
        """
        Attach a payment method to the organization
        param body: Payment method request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PaymentMethodDetails]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.billingv1.payment_method_details import PaymentMethodDetails

        return await self.request_adapter.send_async(request_info, PaymentMethodDetails, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the organization's payment methods.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: UpsertPaymentMethodBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Attach a payment method to the organization
        param body: Payment method request
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
    
    def with_url(self,raw_url: str) -> PaymentMethodsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PaymentMethodsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PaymentMethodsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def from_payment_intent(self) -> FromPaymentIntentRequestBuilder:
        """
        The fromPaymentIntent property
        """
        from .from_payment_intent.from_payment_intent_request_builder import FromPaymentIntentRequestBuilder

        return FromPaymentIntentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def from_setup_intent(self) -> FromSetupIntentRequestBuilder:
        """
        The fromSetupIntent property
        """
        from .from_setup_intent.from_setup_intent_request_builder import FromSetupIntentRequestBuilder

        return FromSetupIntentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PaymentMethodsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PaymentMethodsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

