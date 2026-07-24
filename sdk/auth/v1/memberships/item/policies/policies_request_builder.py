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
    from ......models.auth.v1.list_policies_response import ListPoliciesResponse
    from ......models.auth.v1.policy import Policy
    from .attachments.attachments_request_builder import AttachmentsRequestBuilder
    from .item.with_policy_item_request_builder import WithPolicy_ItemRequestBuilder
    from .policies_post_request_body import PoliciesPostRequestBody

class PoliciesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{org_-id}/policies
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PoliciesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{org_%2Did}/policies{?user_id*}", path_parameters)
    
    def by_policy_id(self,policy_id: str) -> WithPolicy_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.memberships.item.policies.item collection
        param policy_id: Unique identifier of the item
        Returns: WithPolicy_ItemRequestBuilder
        """
        if policy_id is None:
            raise TypeError("policy_id cannot be null.")
        from .item.with_policy_item_request_builder import WithPolicy_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["policy_id"] = policy_id
        return WithPolicy_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PoliciesRequestBuilderGetQueryParameters]] = None) -> Optional[ListPoliciesResponse]:
        """
        ListPolicies
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListPoliciesResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.list_policies_response import ListPoliciesResponse

        return await self.request_adapter.send_async(request_info, ListPoliciesResponse, None)
    
    async def post(self,body: PoliciesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Policy]:
        """
        CreatePolicy
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Policy]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.auth.v1.policy import Policy

        return await self.request_adapter.send_async(request_info, Policy, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PoliciesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListPolicies
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PoliciesPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        CreatePolicy
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
    
    def with_url(self,raw_url: str) -> PoliciesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PoliciesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PoliciesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def attachments(self) -> AttachmentsRequestBuilder:
        """
        The attachments property
        """
        from .attachments.attachments_request_builder import AttachmentsRequestBuilder

        return AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PoliciesRequestBuilderGetQueryParameters():
        """
        ListPolicies
        """
        user_id: Optional[str] = None

    
    @dataclass
    class PoliciesRequestBuilderGetRequestConfiguration(RequestConfiguration[PoliciesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PoliciesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

