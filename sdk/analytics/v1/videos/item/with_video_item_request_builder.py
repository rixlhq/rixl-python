from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .heatmap.heatmap_request_builder import HeatmapRequestBuilder
    from .hot_segments.hot_segments_request_builder import HotSegmentsRequestBuilder
    from .stats.stats_request_builder import StatsRequestBuilder

class WithVideoItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /analytics/v1/videos/{videoId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithVideoItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/analytics/v1/videos/{videoId}", path_parameters)
    
    @property
    def heatmap(self) -> HeatmapRequestBuilder:
        """
        The heatmap property
        """
        from .heatmap.heatmap_request_builder import HeatmapRequestBuilder

        return HeatmapRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hot_segments(self) -> HotSegmentsRequestBuilder:
        """
        The hotSegments property
        """
        from .hot_segments.hot_segments_request_builder import HotSegmentsRequestBuilder

        return HotSegmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stats(self) -> StatsRequestBuilder:
        """
        The stats property
        """
        from .stats.stats_request_builder import StatsRequestBuilder

        return StatsRequestBuilder(self.request_adapter, self.path_parameters)
    

