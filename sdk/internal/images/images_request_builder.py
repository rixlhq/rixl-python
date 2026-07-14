from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mark_failed.mark_failed_request_builder import MarkFailedRequestBuilder
    from .mark_processed.mark_processed_request_builder import MarkProcessedRequestBuilder
    from .take.take_request_builder import TakeRequestBuilder

class ImagesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /internal/images
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ImagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/internal/images", path_parameters)
    
    @property
    def mark_failed(self) -> MarkFailedRequestBuilder:
        """
        The markFailed property
        """
        from .mark_failed.mark_failed_request_builder import MarkFailedRequestBuilder

        return MarkFailedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_processed(self) -> MarkProcessedRequestBuilder:
        """
        The markProcessed property
        """
        from .mark_processed.mark_processed_request_builder import MarkProcessedRequestBuilder

        return MarkProcessedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def take(self) -> TakeRequestBuilder:
        """
        The take property
        """
        from .take.take_request_builder import TakeRequestBuilder

        return TakeRequestBuilder(self.request_adapter, self.path_parameters)
    

