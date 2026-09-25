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
    from ....models.analytics.v1.create_dashboard_request import CreateDashboardRequest
    from ....models.analytics.v1.dashboard import Dashboard
    from ....models.analytics.v1.list_dashboards_response import ListDashboardsResponse
    from .item.dashboard_item_request_builder import Dashboard_ItemRequestBuilder
    from .widgets.widgets_request_builder import WidgetsRequestBuilder

class DashboardsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /analytics/v1/dashboards
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DashboardsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/analytics/v1/dashboards{?page*,page_size*}", path_parameters)
    
    def by_dashboard_id(self,dashboard_id: str) -> Dashboard_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.analytics.v1.dashboards.item collection
        param dashboard_id: Unique identifier of the item
        Returns: Dashboard_ItemRequestBuilder
        """
        if dashboard_id is None:
            raise TypeError("dashboard_id cannot be null.")
        from .item.dashboard_item_request_builder import Dashboard_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dashboard_%2Did"] = dashboard_id
        return Dashboard_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DashboardsRequestBuilderGetQueryParameters]] = None) -> Optional[ListDashboardsResponse]:
        """
        ListDashboards
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListDashboardsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.analytics.v1.list_dashboards_response import ListDashboardsResponse

        return await self.request_adapter.send_async(request_info, ListDashboardsResponse, None)
    
    async def post(self,body: CreateDashboardRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Dashboard]:
        """
        CreateDashboard
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Dashboard]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.analytics.v1.dashboard import Dashboard

        return await self.request_adapter.send_async(request_info, Dashboard, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DashboardsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListDashboards
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateDashboardRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        CreateDashboard
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
    
    def with_url(self,raw_url: str) -> DashboardsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DashboardsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DashboardsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def widgets(self) -> WidgetsRequestBuilder:
        """
        The widgets property
        """
        from .widgets.widgets_request_builder import WidgetsRequestBuilder

        return WidgetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DashboardsRequestBuilderGetQueryParameters():
        """
        ListDashboards
        """
        page: Optional[int] = None

        page_size: Optional[int] = None

    
    @dataclass
    class DashboardsRequestBuilderGetRequestConfiguration(RequestConfiguration[DashboardsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DashboardsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

