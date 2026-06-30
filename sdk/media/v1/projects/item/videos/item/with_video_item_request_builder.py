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
    from .......models.videosv1.delete_result import DeleteResult
    from .......models.videosv1.get_video_response import GetVideoResponse
    from .audio_tracks.audio_tracks_request_builder import AudioTracksRequestBuilder
    from .chapters.chapters_request_builder import ChaptersRequestBuilder
    from .subtitles.subtitles_request_builder import SubtitlesRequestBuilder
    from .thumbnail.thumbnail_request_builder import ThumbnailRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder
    from .visibility.visibility_request_builder import VisibilityRequestBuilder

class WithVideoItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/projects/{projectId}/videos/{videoId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithVideoItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/projects/{projectId}/videos/{videoId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeleteResult]:
        """
        Deletes a video from a project.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeleteResult]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.videosv1.delete_result import DeleteResult

        return await self.request_adapter.send_async(request_info, DeleteResult, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GetVideoResponse]:
        """
        Returns a single video within a project, including private media. Requires project access.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetVideoResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.videosv1.get_video_response import GetVideoResponse

        return await self.request_adapter.send_async(request_info, GetVideoResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a video from a project.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single video within a project, including private media. Requires project access.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithVideoItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithVideoItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithVideoItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def audio_tracks(self) -> AudioTracksRequestBuilder:
        """
        The audioTracks property
        """
        from .audio_tracks.audio_tracks_request_builder import AudioTracksRequestBuilder

        return AudioTracksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chapters(self) -> ChaptersRequestBuilder:
        """
        The chapters property
        """
        from .chapters.chapters_request_builder import ChaptersRequestBuilder

        return ChaptersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subtitles(self) -> SubtitlesRequestBuilder:
        """
        The subtitles property
        """
        from .subtitles.subtitles_request_builder import SubtitlesRequestBuilder

        return SubtitlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thumbnail(self) -> ThumbnailRequestBuilder:
        """
        The thumbnail property
        """
        from .thumbnail.thumbnail_request_builder import ThumbnailRequestBuilder

        return ThumbnailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def visibility(self) -> VisibilityRequestBuilder:
        """
        The visibility property
        """
        from .visibility.visibility_request_builder import VisibilityRequestBuilder

        return VisibilityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithVideoItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithVideoItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

