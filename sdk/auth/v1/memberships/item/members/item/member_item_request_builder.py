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
    from .......models.google.protobuf.empty import Empty
    from .policies.policies_request_builder import PoliciesRequestBuilder
    from .role.role_request_builder import RoleRequestBuilder

class Member_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{org_-id}/members/{member_-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new Member_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{org_%2Did}/members/{member_%2Did}{?user%2Eactor_id*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[Member_ItemRequestBuilderDeleteQueryParameters]] = None) -> Optional[Empty]:
        """
        RemoveMember
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
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[Member_ItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        RemoveMember
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> Member_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Member_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Member_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def policies(self) -> PoliciesRequestBuilder:
        """
        The policies property
        """
        from .policies.policies_request_builder import PoliciesRequestBuilder

        return PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role(self) -> RoleRequestBuilder:
        """
        The role property
        """
        from .role.role_request_builder import RoleRequestBuilder

        return RoleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class Member_ItemRequestBuilderDeleteQueryParameters():
        """
        RemoveMember
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "user_actor_id":
                return "user%2Eactor_id"
            return original_name
        
        user_actor_id: Optional[str] = None

    
    @dataclass
    class Member_ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[Member_ItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

