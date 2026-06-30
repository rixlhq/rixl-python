from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_org_item_request_builder import WithOrgItemRequestBuilder

class OrganizationRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /organization
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrganizationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organization", path_parameters)
    
    def by_org_id(self,org_id: str) -> WithOrgItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.organization.item collection
        param org_id: Organization ID
        Returns: WithOrgItemRequestBuilder
        """
        if org_id is None:
            raise TypeError("org_id cannot be null.")
        from .item.with_org_item_request_builder import WithOrgItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["orgId"] = org_id
        return WithOrgItemRequestBuilder(self.request_adapter, url_tpl_params)
    

