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
    from .......models.auth.v1.policy import Policy
    from .......models.google.protobuf.empty import Empty
    from .attachments.attachments_request_builder import AttachmentsRequestBuilder
    from .with_policy_put_request_body import WithPolicy_PutRequestBody

class WithPolicy_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{org_-id}/policies/{policy_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithPolicy_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{org_%2Did}/policies/{policy_id}{?user%2Euser_id*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[WithPolicy_ItemRequestBuilderDeleteQueryParameters]] = None) -> Optional[Empty]:
        """
        DeletePolicy
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Empty]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.google.protobuf.empty import Empty

        return await self.request_adapter.send_async(request_info, Empty, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithPolicy_ItemRequestBuilderGetQueryParameters]] = None) -> Optional[Policy]:
        """
        GetPolicy
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Policy]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.auth.v1.policy import Policy

        return await self.request_adapter.send_async(request_info, Policy, None)
    
    async def put(self,body: WithPolicy_PutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Policy]:
        """
        UpdatePolicy
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Policy]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.auth.v1.policy import Policy

        return await self.request_adapter.send_async(request_info, Policy, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[WithPolicy_ItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        DeletePolicy
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithPolicy_ItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        GetPolicy
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: WithPolicy_PutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        UpdatePolicy
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
    
    def with_url(self,raw_url: str) -> WithPolicy_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithPolicy_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithPolicy_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def attachments(self) -> AttachmentsRequestBuilder:
        """
        The attachments property
        """
        from .attachments.attachments_request_builder import AttachmentsRequestBuilder

        return AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithPolicy_ItemRequestBuilderDeleteQueryParameters():
        """
        DeletePolicy
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "user_user_id":
                return "user%2Euser_id"
            return original_name
        
        user_user_id: Optional[str] = None

    
    @dataclass
    class WithPolicy_ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[WithPolicy_ItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithPolicy_ItemRequestBuilderGetQueryParameters():
        """
        GetPolicy
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "user_user_id":
                return "user%2Euser_id"
            return original_name
        
        user_user_id: Optional[str] = None

    
    @dataclass
    class WithPolicy_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithPolicy_ItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithPolicy_ItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

