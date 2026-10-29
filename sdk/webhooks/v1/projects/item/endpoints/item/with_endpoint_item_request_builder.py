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
    from .......models.google.protobuf.empty import Empty
    from .......models.webhooks.v1.get_endpoint_response import GetEndpointResponse
    from .......models.webhooks.v1.update_endpoint_response import UpdateEndpointResponse
    from .attempts.attempts_request_builder import AttemptsRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .rotate_secret.rotate_secret_request_builder import RotateSecretRequestBuilder
    from .test.test_request_builder import TestRequestBuilder
    from .with_endpoint_patch_request_body import WithEndpoint_PatchRequestBody

class WithEndpoint_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithEndpoint_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/webhooks/v1/projects/{project_id}/endpoints/{endpoint_id}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Empty]:
        """
        DeleteEndpoint
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Empty]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.google.protobuf.empty import Empty

        return await self.request_adapter.send_async(request_info, Empty, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GetEndpointResponse]:
        """
        GetEndpoint
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetEndpointResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.webhooks.v1.get_endpoint_response import GetEndpointResponse

        return await self.request_adapter.send_async(request_info, GetEndpointResponse, None)
    
    async def patch(self,body: WithEndpoint_PatchRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UpdateEndpointResponse]:
        """
        UpdateEndpoint
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UpdateEndpointResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.webhooks.v1.update_endpoint_response import UpdateEndpointResponse

        return await self.request_adapter.send_async(request_info, UpdateEndpointResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        DeleteEndpoint
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        GetEndpoint
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WithEndpoint_PatchRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        UpdateEndpoint
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
    
    def with_url(self,raw_url: str) -> WithEndpoint_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithEndpoint_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithEndpoint_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def attempts(self) -> AttemptsRequestBuilder:
        """
        The attempts property
        """
        from .attempts.attempts_request_builder import AttemptsRequestBuilder

        return AttemptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        The events property
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rotate_secret(self) -> RotateSecretRequestBuilder:
        """
        The rotateSecret property
        """
        from .rotate_secret.rotate_secret_request_builder import RotateSecretRequestBuilder

        return RotateSecretRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def test(self) -> TestRequestBuilder:
        """
        The test property
        """
        from .test.test_request_builder import TestRequestBuilder

        return TestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithEndpoint_ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithEndpoint_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithEndpoint_ItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

