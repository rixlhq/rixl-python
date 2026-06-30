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
    from ........models.gateway.update_chapters_body import UpdateChaptersBody
    from ........models.videosv1.video_chapters import VideoChapters
    from .item.with_start_time_sec_item_request_builder import WithStartTimeSecItemRequestBuilder

class ChaptersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/projects/{projectId}/videos/{videoId}/chapters
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChaptersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/projects/{projectId}/videos/{videoId}/chapters", path_parameters)
    
    def by_start_time_sec(self,start_time_sec: int) -> WithStartTimeSecItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.v1.projects.item.videos.item.chapters.item collection
        param start_time_sec: Chapter start time (seconds)
        Returns: WithStartTimeSecItemRequestBuilder
        """
        if start_time_sec is None:
            raise TypeError("start_time_sec cannot be null.")
        from .item.with_start_time_sec_item_request_builder import WithStartTimeSecItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["startTimeSec"] = start_time_sec
        return WithStartTimeSecItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VideoChapters]:
        """
        Removes every chapter from a video.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VideoChapters]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.videosv1.video_chapters import VideoChapters

        return await self.request_adapter.send_async(request_info, VideoChapters, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VideoChapters]:
        """
        Returns the chapters of a video.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VideoChapters]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.videosv1.video_chapters import VideoChapters

        return await self.request_adapter.send_async(request_info, VideoChapters, None)
    
    async def put(self,body: UpdateChaptersBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[VideoChapters]:
        """
        Replaces the chapters of a video.
        param body: Chapters to set
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VideoChapters]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.videosv1.video_chapters import VideoChapters

        return await self.request_adapter.send_async(request_info, VideoChapters, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes every chapter from a video.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the chapters of a video.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: UpdateChaptersBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces the chapters of a video.
        param body: Chapters to set
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ChaptersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChaptersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChaptersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ChaptersRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChaptersRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChaptersRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

