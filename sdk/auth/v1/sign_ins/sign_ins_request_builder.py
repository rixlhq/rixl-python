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
    from ....models.auth.v1.list_sign_ins_response import ListSignInsResponse
    from ....models.google.rpc.status import Status
    from .item.with_sign_in_item_request_builder import WithSign_in_ItemRequestBuilder
    from .revoke_others.revoke_others_request_builder import RevokeOthersRequestBuilder

class SignInsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/sign-ins
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SignInsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/sign-ins{?user_id*}", path_parameters)
    
    def by_sign_in_id(self,sign_in_id: str) -> WithSign_in_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.signIns.item collection
        param sign_in_id: Unique identifier of the item
        Returns: WithSign_in_ItemRequestBuilder
        """
        if sign_in_id is None:
            raise TypeError("sign_in_id cannot be null.")
        from .item.with_sign_in_item_request_builder import WithSign_in_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sign_in_id"] = sign_in_id
        return WithSign_in_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SignInsRequestBuilderGetQueryParameters]] = None) -> Optional[ListSignInsResponse]:
        """
        Lists the caller's sign-ins, most recently used first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListSignInsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.google.rpc.status import Status

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Status,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.auth.v1.list_sign_ins_response import ListSignInsResponse

        return await self.request_adapter.send_async(request_info, ListSignInsResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SignInsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists the caller's sign-ins, most recently used first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> SignInsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SignInsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SignInsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def revoke_others(self) -> RevokeOthersRequestBuilder:
        """
        The revokeOthers property
        """
        from .revoke_others.revoke_others_request_builder import RevokeOthersRequestBuilder

        return RevokeOthersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SignInsRequestBuilderGetQueryParameters():
        """
        Lists the caller's sign-ins, most recently used first.
        """
        user_id: Optional[str] = None

    
    @dataclass
    class SignInsRequestBuilderGetRequestConfiguration(RequestConfiguration[SignInsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

