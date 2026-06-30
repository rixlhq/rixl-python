from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active.active_request_builder import ActiveRequestBuilder
    from .check.check_request_builder import CheckRequestBuilder
    from .domain.domain_request_builder import DomainRequestBuilder
    from .info.info_request_builder import InfoRequestBuilder
    from .leave.leave_request_builder import LeaveRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .membership.membership_request_builder import MembershipRequestBuilder
    from .name.name_request_builder import NameRequestBuilder
    from .policies.policies_request_builder import PoliciesRequestBuilder
    from .username.username_request_builder import UsernameRequestBuilder

class WithOrgItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{orgId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithOrgItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{orgId}", path_parameters)
    
    @property
    def active(self) -> ActiveRequestBuilder:
        """
        The active property
        """
        from .active.active_request_builder import ActiveRequestBuilder

        return ActiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check(self) -> CheckRequestBuilder:
        """
        The check property
        """
        from .check.check_request_builder import CheckRequestBuilder

        return CheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain(self) -> DomainRequestBuilder:
        """
        The domain property
        """
        from .domain.domain_request_builder import DomainRequestBuilder

        return DomainRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def leave(self) -> LeaveRequestBuilder:
        """
        The leave property
        """
        from .leave.leave_request_builder import LeaveRequestBuilder

        return LeaveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        The members property
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def membership(self) -> MembershipRequestBuilder:
        """
        The membership property
        """
        from .membership.membership_request_builder import MembershipRequestBuilder

        return MembershipRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def name(self) -> NameRequestBuilder:
        """
        The name property
        """
        from .name.name_request_builder import NameRequestBuilder

        return NameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> PoliciesRequestBuilder:
        """
        The policies property
        """
        from .policies.policies_request_builder import PoliciesRequestBuilder

        return PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def username(self) -> UsernameRequestBuilder:
        """
        The username property
        """
        from .username.username_request_builder import UsernameRequestBuilder

        return UsernameRequestBuilder(self.request_adapter, self.path_parameters)
    

