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
    from ......models.auth.v1.list_org_members_response import ListOrgMembersResponse
    from .item.member_item_request_builder import Member_ItemRequestBuilder

class MembersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{org_-id}/members
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MembersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{org_%2Did}/members{?limit*,offset*,user%2EuserId*}", path_parameters)
    
    def by_member_id(self,member_id: str) -> Member_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.memberships.item.members.item collection
        param member_id: Unique identifier of the item
        Returns: Member_ItemRequestBuilder
        """
        if member_id is None:
            raise TypeError("member_id cannot be null.")
        from .item.member_item_request_builder import Member_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["member_%2Did"] = member_id
        return Member_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MembersRequestBuilderGetQueryParameters]] = None) -> Optional[ListOrgMembersResponse]:
        """
        ListOrganizationMembers
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListOrgMembersResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.list_org_members_response import ListOrgMembersResponse

        return await self.request_adapter.send_async(request_info, ListOrgMembersResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MembersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListOrganizationMembers
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MembersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MembersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MembersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MembersRequestBuilderGetQueryParameters():
        """
        ListOrganizationMembers
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
                return "user%2EuserId"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            return original_name
        
        limit: Optional[int] = None

        offset: Optional[int] = None

        user_user_id: Optional[str] = None

    
    @dataclass
    class MembersRequestBuilderGetRequestConfiguration(RequestConfiguration[MembersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

