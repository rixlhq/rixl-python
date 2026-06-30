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
    from ....models.clientauthv1.create_client_credential_response import CreateClientCredentialResponse
    from ....models.clientauthv1.list_client_credentials_response import ListClientCredentialsResponse
    from ....models.types.create_client_credential_request import CreateClientCredentialRequest
    from .item.with_credential_item_request_builder import WithCredentialItemRequestBuilder

class CredentialsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /platform/clientauth/credentials
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CredentialsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/platform/clientauth/credentials{?limit*,offset*}", path_parameters)
    
    def by_credential_id(self,credential_id: str) -> WithCredentialItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.platform.clientauth.credentials.item collection
        param credential_id: Client credential ID
        Returns: WithCredentialItemRequestBuilder
        """
        if credential_id is None:
            raise TypeError("credential_id cannot be null.")
        from .item.with_credential_item_request_builder import WithCredentialItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["credentialId"] = credential_id
        return WithCredentialItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CredentialsRequestBuilderGetQueryParameters]] = None) -> Optional[ListClientCredentialsResponse]:
        """
        List client credentials for the specified organization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListClientCredentialsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.clientauthv1.list_client_credentials_response import ListClientCredentialsResponse

        return await self.request_adapter.send_async(request_info, ListClientCredentialsResponse, None)
    
    async def post(self,body: CreateClientCredentialRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CreateClientCredentialResponse]:
        """
        Create a new client credential for the authenticated organization
        param body: Client credential creation request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreateClientCredentialResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.clientauthv1.create_client_credential_response import CreateClientCredentialResponse

        return await self.request_adapter.send_async(request_info, CreateClientCredentialResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CredentialsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        List client credentials for the specified organization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateClientCredentialRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new client credential for the authenticated organization
        param body: Client credential creation request
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
    
    def with_url(self,raw_url: str) -> CredentialsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CredentialsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CredentialsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CredentialsRequestBuilderGetQueryParameters():
        """
        List client credentials for the specified organization
        """
        # Pagination limit
        limit: Optional[int] = None

        # Pagination offset
        offset: Optional[int] = None

    
    @dataclass
    class CredentialsRequestBuilderGetRequestConfiguration(RequestConfiguration[CredentialsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CredentialsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

