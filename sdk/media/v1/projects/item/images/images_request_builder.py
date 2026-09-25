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
    from ......models.images.v1.list_images_response import ListImagesResponse
    from .item.with_image_item_request_builder import WithImage_ItemRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class ImagesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/projects/{project_id}/images
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ImagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/projects/{project_id}/images{?pagination%2Elimit*,pagination%2Eoffset*,sort_direction*,sort_field*}", path_parameters)
    
    def by_image_id(self,image_id: str) -> WithImage_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.v1.projects.item.images.item collection
        param image_id: Unique identifier of the item
        Returns: WithImage_ItemRequestBuilder
        """
        if image_id is None:
            raise TypeError("image_id cannot be null.")
        from .item.with_image_item_request_builder import WithImage_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["image_id"] = image_id
        return WithImage_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ImagesRequestBuilderGetQueryParameters]] = None) -> Optional[ListImagesResponse]:
        """
        ListImages
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListImagesResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.images.v1.list_images_response import ListImagesResponse

        return await self.request_adapter.send_async(request_info, ListImagesResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ImagesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        ListImages
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ImagesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ImagesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ImagesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ImagesRequestBuilderGetQueryParameters():
        """
        ListImages
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
                return "sort_direction"
            if original_name == "sort_field":
                return "sort_field"
            return original_name
        
        # Maximum number of items to return.
        pagination_limit: Optional[int] = None

        # Number of items to skip before collecting the result set.
        pagination_offset: Optional[int] = None

        sort_direction: Optional[str] = None

        sort_field: Optional[str] = None

    
    @dataclass
    class ImagesRequestBuilderGetRequestConfiguration(RequestConfiguration[ImagesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

