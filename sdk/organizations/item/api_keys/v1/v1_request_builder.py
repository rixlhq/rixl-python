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
    from .....models.apikeys.v1.create_api_key_response import CreateApiKeyResponse
    from .....models.apikeys.v1.list_api_keys_response import ListApiKeysResponse
    from .item.with_key_item_request_builder import WithKey_ItemRequestBuilder
    from .v1_post_request_body import V1PostRequestBody

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /organizations/{org_id}/api-keys/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organizations/{org_id}/api-keys/v1{?pagination%2Elimit*,pagination%2Eoffset*}", path_parameters)
    
    def by_key_id(self,key_id: str) -> WithKey_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.organizations.item.apiKeys.v1.item collection
        param key_id: Unique identifier of the item
        Returns: WithKey_ItemRequestBuilder
        """
        if key_id is None:
            raise TypeError("key_id cannot be null.")
        from .item.with_key_item_request_builder import WithKey_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["key_id"] = key_id
        return WithKey_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[V1RequestBuilderGetQueryParameters]] = None) -> Optional[ListApiKeysResponse]:
        """
        ListApiKeys
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListApiKeysResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.apikeys.v1.list_api_keys_response import ListApiKeysResponse

        return await self.request_adapter.send_async(request_info, ListApiKeysResponse, None)
    
    async def post(self,body: V1PostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CreateApiKeyResponse]:
        """
        CreateApiKey
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreateApiKeyResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.apikeys.v1.create_api_key_response import CreateApiKeyResponse

        return await self.request_adapter.send_async(request_info, CreateApiKeyResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[V1RequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListApiKeys
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: V1PostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        CreateApiKey
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> V1RequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: V1RequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return V1RequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class V1RequestBuilderGetQueryParameters():
        """
        ListApiKeys
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "pagination_limit":
                return "pagination%2Elimit"
            if original_name == "pagination_offset":
                return "pagination%2Eoffset"
            return original_name
        
        # Maximum number of items to return.
        pagination_limit: Optional[int] = None

        # Number of items to skip before collecting the result set.
        pagination_offset: Optional[int] = None

    
    @dataclass
    class V1RequestBuilderGetRequestConfiguration(RequestConfiguration[V1RequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class V1RequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

