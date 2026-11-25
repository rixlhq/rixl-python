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
    from ......models.auth.v1.invitation import Invitation
    from ......models.auth.v1.invitation_state import InvitationState
    from ......models.auth.v1.list_organization_invitations_response import ListOrganizationInvitationsResponse
    from ......models.google.rpc.status import Status
    from .invitations_post_request_body import InvitationsPostRequestBody
    from .item.with_invitation_item_request_builder import WithInvitation_ItemRequestBuilder

class InvitationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/organizations/{org_id}/invitations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvitationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/organizations/{org_id}/invitations{?page_size*,page_token*,state*}", path_parameters)
    
    def by_invitation_id(self,invitation_id: str) -> WithInvitation_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.organizations.item.invitations.item collection
        param invitation_id: Unique identifier of the item
        Returns: WithInvitation_ItemRequestBuilder
        """
        if invitation_id is None:
            raise TypeError("invitation_id cannot be null.")
        from .item.with_invitation_item_request_builder import WithInvitation_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["invitation_id"] = invitation_id
        return WithInvitation_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InvitationsRequestBuilderGetQueryParameters]] = None) -> Optional[ListOrganizationInvitationsResponse]:
        """
        ListOrganizationInvitations
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListOrganizationInvitationsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.google.rpc.status import Status

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Status,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.list_organization_invitations_response import ListOrganizationInvitationsResponse

        return await self.request_adapter.send_async(request_info, ListOrganizationInvitationsResponse, error_mapping)
    
    async def post(self,body: InvitationsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Invitation]:
        """
        CreateInvitation
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Invitation]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.google.rpc.status import Status

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Status,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.invitation import Invitation

        return await self.request_adapter.send_async(request_info, Invitation, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InvitationsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListOrganizationInvitations
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: InvitationsPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        CreateInvitation
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
    
    def with_url(self,raw_url: str) -> InvitationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InvitationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InvitationsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class InvitationsRequestBuilderGetQueryParameters():
        """
        ListOrganizationInvitations
        """
        page_size: Optional[int] = None

        page_token: Optional[str] = None

        # Defaults to pending.
        state: Optional[InvitationState] = None

    
    @dataclass
    class InvitationsRequestBuilderGetRequestConfiguration(RequestConfiguration[InvitationsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InvitationsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

