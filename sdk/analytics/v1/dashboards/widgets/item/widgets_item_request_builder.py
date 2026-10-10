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
    from ......models.analytics.v1.delete_widget_response import DeleteWidgetResponse
    from ......models.analytics.v1.widget import Widget
    from .widgets_patch_request_body import WidgetsPatchRequestBody

class WidgetsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /analytics/v1/dashboards/widgets/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WidgetsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/analytics/v1/dashboards/widgets/{id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[WidgetsItemRequestBuilderDeleteQueryParameters]] = None) -> Optional[DeleteWidgetResponse]:
        """
        DeleteWidget
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeleteWidgetResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.analytics.v1.delete_widget_response import DeleteWidgetResponse

        return await self.request_adapter.send_async(request_info, DeleteWidgetResponse, None)
    
    async def patch(self,body: WidgetsPatchRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Widget]:
        """
        UpdateWidget
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Widget]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.analytics.v1.widget import Widget

        return await self.request_adapter.send_async(request_info, Widget, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[WidgetsItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        DeleteWidget
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/analytics/v1/dashboards/widgets/{id}?expected_revision={expected_revision}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WidgetsPatchRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        UpdateWidget
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
    
    def with_url(self,raw_url: str) -> WidgetsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WidgetsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WidgetsItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WidgetsItemRequestBuilderDeleteQueryParameters():
        """
        DeleteWidget
        """
        expected_revision: Optional[int] = None

    
    @dataclass
    class WidgetsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[WidgetsItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WidgetsItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

