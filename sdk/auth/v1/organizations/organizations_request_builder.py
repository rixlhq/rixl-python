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
    from ....models.auth.v1.create_organization_request import CreateOrganizationRequest
    from ....models.auth.v1.list_organizations_response import ListOrganizationsResponse
    from ....models.auth.v1.organization import Organization
    from ....models.error import Error
    from .item.with_org_item_request_builder import WithOrg_ItemRequestBuilder

class OrganizationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/organizations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrganizationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/organizations{?page_size*,page_token*,show_deleted*}", path_parameters)
    
    def by_org_id(self,org_id: str) -> WithOrg_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.organizations.item collection
        param org_id: Unique identifier of the item
        Returns: WithOrg_ItemRequestBuilder
        """
        if org_id is None:
            raise TypeError("org_id cannot be null.")
        from .item.with_org_item_request_builder import WithOrg_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["org_id"] = org_id
        return WithOrg_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OrganizationsRequestBuilderGetQueryParameters]] = None) -> Optional[ListOrganizationsResponse]:
        """
        ListOrganizations
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListOrganizationsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.error import Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.auth.v1.list_organizations_response import ListOrganizationsResponse

        return await self.request_adapter.send_async(request_info, ListOrganizationsResponse, error_mapping)
    
    async def post(self,body: CreateOrganizationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Organization]:
        """
        CreateOrganization
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Organization]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.error import Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.auth.v1.organization import Organization

        return await self.request_adapter.send_async(request_info, Organization, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OrganizationsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListOrganizations
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateOrganizationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        CreateOrganization
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
    
    def with_url(self,raw_url: str) -> OrganizationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OrganizationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OrganizationsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class OrganizationsRequestBuilderGetQueryParameters():
        """
        ListOrganizations
        """
        page_size: Optional[int] = None

        page_token: Optional[str] = None

        # Includes deleted organizations visible to their retained active owners.
        show_deleted: Optional[bool] = None

    
    @dataclass
    class OrganizationsRequestBuilderGetRequestConfiguration(RequestConfiguration[OrganizationsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OrganizationsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

