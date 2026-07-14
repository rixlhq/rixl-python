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
    from ....models.billing.v1.list_invoices_response import ListInvoicesResponse
    from .item.with_invoice_item_request_builder import WithInvoice_ItemRequestBuilder

class InvoicesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /billing/v1/invoices
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvoicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/billing/v1/invoices{?orgId*,pagination%2Elimit*,pagination%2Eoffset*}", path_parameters)
    
    def by_invoice_id(self,invoice_id: str) -> WithInvoice_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.billing.v1.invoices.item collection
        param invoice_id: Unique identifier of the item
        Returns: WithInvoice_ItemRequestBuilder
        """
        if invoice_id is None:
            raise TypeError("invoice_id cannot be null.")
        from .item.with_invoice_item_request_builder import WithInvoice_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["invoice_id"] = invoice_id
        return WithInvoice_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]] = None) -> Optional[ListInvoicesResponse]:
        """
        ListInvoices
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListInvoicesResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.billing.v1.list_invoices_response import ListInvoicesResponse

        return await self.request_adapter.send_async(request_info, ListInvoicesResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListInvoices
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> InvoicesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InvoicesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InvoicesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class InvoicesRequestBuilderGetQueryParameters():
        """
        ListInvoices
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "org_id":
                return "orgId"
            if original_name == "pagination_limit":
                return "pagination%2Elimit"
            if original_name == "pagination_offset":
                return "pagination%2Eoffset"
            return original_name
        
        org_id: Optional[str] = None

        # Maximum number of items to return.
        pagination_limit: Optional[int] = None

        # Number of items to skip before collecting the result set.
        pagination_offset: Optional[int] = None

    
    @dataclass
    class InvoicesRequestBuilderGetRequestConfiguration(RequestConfiguration[InvoicesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

