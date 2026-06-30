from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .images.images_request_builder import ImagesRequestBuilder
    from .languages.languages_request_builder import LanguagesRequestBuilder
    from .projects.projects_request_builder import ProjectsRequestBuilder
    from .videos.videos_request_builder import VideosRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1", path_parameters)
    
    @property
    def images(self) -> ImagesRequestBuilder:
        """
        The images property
        """
        from .images.images_request_builder import ImagesRequestBuilder

        return ImagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> LanguagesRequestBuilder:
        """
        The languages property
        """
        from .languages.languages_request_builder import LanguagesRequestBuilder

        return LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> ProjectsRequestBuilder:
        """
        The projects property
        """
        from .projects.projects_request_builder import ProjectsRequestBuilder

        return ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def videos(self) -> VideosRequestBuilder:
        """
        The videos property
        """
        from .videos.videos_request_builder import VideosRequestBuilder

        return VideosRequestBuilder(self.request_adapter, self.path_parameters)
    

