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
    from .....models.projectsv1.project import Project
    from .custom_domain.custom_domain_request_builder import CustomDomainRequestBuilder
    from .move.move_request_builder import MoveRequestBuilder
    from .name.name_request_builder import NameRequestBuilder
    from .video_quality.video_quality_request_builder import VideoQualityRequestBuilder

class WithProjectItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /organization/{orgId}/projects/{projectId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProjectItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organization/{orgId}/projects/{projectId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Project]:
        """
        Soft delete a project (marks it as deleted)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Project]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.projectsv1.project import Project

        return await self.request_adapter.send_async(request_info, Project, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Project]:
        """
        Retrieve a specific project under an organization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Project]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.projectsv1.project import Project

        return await self.request_adapter.send_async(request_info, Project, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Soft delete a project (marks it as deleted)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieve a specific project under an organization
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithProjectItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithProjectItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithProjectItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def custom_domain(self) -> CustomDomainRequestBuilder:
        """
        The customDomain property
        """
        from .custom_domain.custom_domain_request_builder import CustomDomainRequestBuilder

        return CustomDomainRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move(self) -> MoveRequestBuilder:
        """
        The move property
        """
        from .move.move_request_builder import MoveRequestBuilder

        return MoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def name(self) -> NameRequestBuilder:
        """
        The name property
        """
        from .name.name_request_builder import NameRequestBuilder

        return NameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def video_quality(self) -> VideoQualityRequestBuilder:
        """
        The videoQuality property
        """
        from .video_quality.video_quality_request_builder import VideoQualityRequestBuilder

        return VideoQualityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithProjectItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithProjectItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

