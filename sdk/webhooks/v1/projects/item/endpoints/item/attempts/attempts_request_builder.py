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
    from ........models.webhooks.v1.list_endpoint_attempts_response import ListEndpointAttemptsResponse

class AttemptsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}/attempts
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AttemptsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}/attempts{?pagination%2Elimit*,pagination%2Eoffset*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AttemptsRequestBuilderGetQueryParameters]] = None) -> Optional[ListEndpointAttemptsResponse]:
        """
        ListEndpointAttempts returns the delivery history for one endpoint, newest first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListEndpointAttemptsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.webhooks.v1.list_endpoint_attempts_response import ListEndpointAttemptsResponse

        return await self.request_adapter.send_async(request_info, ListEndpointAttemptsResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AttemptsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListEndpointAttempts returns the delivery history for one endpoint, newest first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> AttemptsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AttemptsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AttemptsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AttemptsRequestBuilderGetQueryParameters():
        """
        ListEndpointAttempts returns the delivery history for one endpoint, newest first.
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
    class AttemptsRequestBuilderGetRequestConfiguration(RequestConfiguration[AttemptsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

