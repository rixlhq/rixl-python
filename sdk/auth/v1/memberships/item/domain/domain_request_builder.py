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
    from ......models.auth.v1.domain_response import DomainResponse
    from ......models.google.protobuf.empty import Empty
    from .auto_join.auto_join_request_builder import AutoJoinRequestBuilder
    from .domain_post_request_body import DomainPostRequestBody
    from .verify.verify_request_builder import VerifyRequestBuilder

class DomainRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{org_-id}/domain
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DomainRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{org_%2Did}/domain{?user_id*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[DomainRequestBuilderDeleteQueryParameters]] = None) -> Optional[Empty]:
        """
        RemoveDomain
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Empty]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.google.protobuf.empty import Empty

        return await self.request_adapter.send_async(request_info, Empty, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DomainRequestBuilderGetQueryParameters]] = None) -> Optional[DomainResponse]:
        """
        GetDomainStatus
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DomainResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.domain_response import DomainResponse

        return await self.request_adapter.send_async(request_info, DomainResponse, None)
    
    async def post(self,body: DomainPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DomainResponse]:
        """
        CreateDomainVerification
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DomainResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.domain_response import DomainResponse

        return await self.request_adapter.send_async(request_info, DomainResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[DomainRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        RemoveDomain
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DomainRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        GetDomainStatus
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: DomainPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        CreateDomainVerification
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
    
    def with_url(self,raw_url: str) -> DomainRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DomainRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DomainRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def auto_join(self) -> AutoJoinRequestBuilder:
        """
        The autoJoin property
        """
        from .auto_join.auto_join_request_builder import AutoJoinRequestBuilder

        return AutoJoinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify(self) -> VerifyRequestBuilder:
        """
        The verify property
        """
        from .verify.verify_request_builder import VerifyRequestBuilder

        return VerifyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DomainRequestBuilderDeleteQueryParameters():
        """
        RemoveDomain
        """
        user_id: Optional[str] = None

    
    @dataclass
    class DomainRequestBuilderDeleteRequestConfiguration(RequestConfiguration[DomainRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DomainRequestBuilderGetQueryParameters():
        """
        GetDomainStatus
        """
        user_id: Optional[str] = None

    
    @dataclass
    class DomainRequestBuilderGetRequestConfiguration(RequestConfiguration[DomainRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DomainRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

