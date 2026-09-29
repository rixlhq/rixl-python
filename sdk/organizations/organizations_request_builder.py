from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_org_item_request_builder import WithOrg_ItemRequestBuilder

class OrganizationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /organizations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrganizationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organizations", path_parameters)
    
    def by_org_id(self,org_id: str) -> WithOrg_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.organizations.item collection
        param org_id: Unique identifier of the item
        Returns: WithOrg_ItemRequestBuilder
        """
        if org_id is None:
            raise TypeError("org_id cannot be null.")
        from .item.with_org_item_request_builder import WithOrg_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["org_id"] = org_id
        return WithOrg_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

