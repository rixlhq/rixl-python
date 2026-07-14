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
    from ......models.videos.v1.list_videos_response import ListVideosResponse
    from .item.with_video_item_request_builder import WithVideo_ItemRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class VideosRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/projects/{project_id}/videos
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VideosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/projects/{project_id}/videos{?pagination%2Elimit*,pagination%2Eoffset*,sortDirection*,sortField*}", path_parameters)
    
    def by_video_id(self,video_id: str) -> WithVideo_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.v1.projects.item.videos.item collection
        param video_id: Unique identifier of the item
        Returns: WithVideo_ItemRequestBuilder
        """
        if video_id is None:
            raise TypeError("video_id cannot be null.")
        from .item.with_video_item_request_builder import WithVideo_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["video_id"] = video_id
        return WithVideo_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[VideosRequestBuilderGetQueryParameters]] = None) -> Optional[ListVideosResponse]:
        """
        ListVideos
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListVideosResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.videos.v1.list_videos_response import ListVideosResponse

        return await self.request_adapter.send_async(request_info, ListVideosResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[VideosRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListVideos
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> VideosRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VideosRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VideosRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VideosRequestBuilderGetQueryParameters():
        """
        ListVideos
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "pagination_limit":
                return "pagination%2Elimit"
            if original_name == "pagination_offset":
                return "pagination%2Eoffset"
            if original_name == "sort_direction":
                return "sortDirection"
            if original_name == "sort_field":
                return "sortField"
            return original_name
        
        # Maximum number of items to return.
        pagination_limit: Optional[int] = None

        # Number of items to skip before collecting the result set.
        pagination_offset: Optional[int] = None

        sort_direction: Optional[str] = None

        sort_field: Optional[str] = None

    
    @dataclass
    class VideosRequestBuilderGetRequestConfiguration(RequestConfiguration[VideosRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

