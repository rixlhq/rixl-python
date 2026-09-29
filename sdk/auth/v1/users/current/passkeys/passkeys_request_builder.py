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
    from ......models.auth.v1.list_passkeys_response import ListPasskeysResponse
    from .item.passkeys_item_request_builder import PasskeysItemRequestBuilder
    from .register.register_request_builder import RegisterRequestBuilder

class PasskeysRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/users/current/passkeys
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PasskeysRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/users/current/passkeys{?user_id*}", path_parameters)
    
    def by_id(self,id: str) -> PasskeysItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.users.current.passkeys.item collection
        param id: Unique identifier of the item
        Returns: PasskeysItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.passkeys_item_request_builder import PasskeysItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PasskeysItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PasskeysRequestBuilderGetQueryParameters]] = None) -> Optional[ListPasskeysResponse]:
        """
        ListPasskeys
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListPasskeysResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.list_passkeys_response import ListPasskeysResponse

        return await self.request_adapter.send_async(request_info, ListPasskeysResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PasskeysRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListPasskeys
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PasskeysRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PasskeysRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PasskeysRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def register(self) -> RegisterRequestBuilder:
        """
        The register property
        """
        from .register.register_request_builder import RegisterRequestBuilder

        return RegisterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PasskeysRequestBuilderGetQueryParameters():
        """
        ListPasskeys
        """
        user_id: Optional[str] = None

    
    @dataclass
    class PasskeysRequestBuilderGetRequestConfiguration(RequestConfiguration[PasskeysRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

