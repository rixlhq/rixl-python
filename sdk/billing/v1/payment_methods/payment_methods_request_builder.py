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
    from ....models.billing.v1.list_payment_methods_response import ListPaymentMethodsResponse
    from ....models.billing.v1.payment_method_details import PaymentMethodDetails
    from ....models.billing.v1.upsert_payment_method_request import UpsertPaymentMethodRequest
    from .from_payment_intent.from_payment_intent_request_builder import FromPaymentIntentRequestBuilder
    from .from_setup_intent.from_setup_intent_request_builder import FromSetupIntentRequestBuilder
    from .item.with_payment_method_item_request_builder import WithPayment_method_ItemRequestBuilder

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
        super().__init__(request_adapter, "{+baseurl}/billing/v1/payment-methods{?org_id*,refresh*}", path_parameters)
    
    def by_payment_method_id(self,payment_method_id: str) -> WithPayment_method_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.billing.v1.paymentMethods.item collection
        param payment_method_id: Unique identifier of the item
        Returns: WithPayment_method_ItemRequestBuilder
        """
        if payment_method_id is None:
            raise TypeError("payment_method_id cannot be null.")
        from .item.with_payment_method_item_request_builder import WithPayment_method_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["payment_method_id"] = payment_method_id
        return WithPayment_method_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PaymentMethodsRequestBuilderGetQueryParameters]] = None) -> Optional[ListPaymentMethodsResponse]:
        """
        ListPaymentMethods
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListPaymentMethodsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.billing.v1.list_payment_methods_response import ListPaymentMethodsResponse

        return await self.request_adapter.send_async(request_info, ListPaymentMethodsResponse, None)
    
    async def put(self,body: UpsertPaymentMethodRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PaymentMethodDetails]:
        """
        UpsertPaymentMethod
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PaymentMethodDetails]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.billing.v1.payment_method_details import PaymentMethodDetails

        return await self.request_adapter.send_async(request_info, PaymentMethodDetails, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PaymentMethodsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListPaymentMethods
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: UpsertPaymentMethodRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        UpsertPaymentMethod
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
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
    class PaymentMethodsRequestBuilderGetQueryParameters():
        """
        ListPaymentMethods
        """
        org_id: Optional[str] = None

        refresh: Optional[bool] = None

    
    @dataclass
    class PaymentMethodsRequestBuilderGetRequestConfiguration(RequestConfiguration[PaymentMethodsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PaymentMethodsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

