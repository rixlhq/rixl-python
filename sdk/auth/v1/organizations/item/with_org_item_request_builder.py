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
    from .....models.auth.v1.organization import Organization
    from .....models.google.rpc.status import Status
    from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder
    from .avatar.avatar_request_builder import AvatarRequestBuilder
    from .convert_to_team.convert_to_team_request_builder import ConvertToTeamRequestBuilder
    from .domain.domain_request_builder import DomainRequestBuilder
    from .invitations.invitations_request_builder import InvitationsRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .policies.policies_request_builder import PoliciesRequestBuilder
    from .transfer_ownership.transfer_ownership_request_builder import TransferOwnershipRequestBuilder
    from .with_org_patch_request_body import WithOrg_PatchRequestBody

class WithOrg_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/organizations/{org_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithOrg_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/organizations/{org_id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Organization]:
        """
        GetOrganization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Organization]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.google.rpc.status import Status

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Status,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.auth.v1.organization import Organization

        return await self.request_adapter.send_async(request_info, Organization, error_mapping)
    
    async def patch(self,body: WithOrg_PatchRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Organization]:
        """
        UpdateOrganization
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Organization]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.google.rpc.status import Status

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Status,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.auth.v1.organization import Organization

        return await self.request_adapter.send_async(request_info, Organization, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        GetOrganization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WithOrg_PatchRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        UpdateOrganization
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithOrg_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithOrg_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithOrg_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def audit_events(self) -> AuditEventsRequestBuilder:
        """
        The auditEvents property
        """
        from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder

        return AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def avatar(self) -> AvatarRequestBuilder:
        """
        The avatar property
        """
        from .avatar.avatar_request_builder import AvatarRequestBuilder

        return AvatarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def convert_to_team(self) -> ConvertToTeamRequestBuilder:
        """
        The convertToTeam property
        """
        from .convert_to_team.convert_to_team_request_builder import ConvertToTeamRequestBuilder

        return ConvertToTeamRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain(self) -> DomainRequestBuilder:
        """
        The domain property
        """
        from .domain.domain_request_builder import DomainRequestBuilder

        return DomainRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invitations(self) -> InvitationsRequestBuilder:
        """
        The invitations property
        """
        from .invitations.invitations_request_builder import InvitationsRequestBuilder

        return InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        The members property
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> PoliciesRequestBuilder:
        """
        The policies property
        """
        from .policies.policies_request_builder import PoliciesRequestBuilder

        return PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transfer_ownership(self) -> TransferOwnershipRequestBuilder:
        """
        The transferOwnership property
        """
        from .transfer_ownership.transfer_ownership_request_builder import TransferOwnershipRequestBuilder

        return TransferOwnershipRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithOrg_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithOrg_ItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

