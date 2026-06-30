from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dashboard.dashboard_request_builder import DashboardRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .feeds.feeds_request_builder import FeedsRequestBuilder
    from .funnels.funnels_request_builder import FunnelsRequestBuilder
    from .posts.posts_request_builder import PostsRequestBuilder
    from .realtime.realtime_request_builder import RealtimeRequestBuilder
    from .retention.retention_request_builder import RetentionRequestBuilder
    from .top.top_request_builder import TopRequestBuilder
    from .videos.videos_request_builder import VideosRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /analytics/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/analytics/v1", path_parameters)
    
    @property
    def dashboard(self) -> DashboardRequestBuilder:
        """
        The dashboard property
        """
        from .dashboard.dashboard_request_builder import DashboardRequestBuilder

        return DashboardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        The events property
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def feeds(self) -> FeedsRequestBuilder:
        """
        The feeds property
        """
        from .feeds.feeds_request_builder import FeedsRequestBuilder

        return FeedsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def funnels(self) -> FunnelsRequestBuilder:
        """
        The funnels property
        """
        from .funnels.funnels_request_builder import FunnelsRequestBuilder

        return FunnelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def posts(self) -> PostsRequestBuilder:
        """
        The posts property
        """
        from .posts.posts_request_builder import PostsRequestBuilder

        return PostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def realtime(self) -> RealtimeRequestBuilder:
        """
        The realtime property
        """
        from .realtime.realtime_request_builder import RealtimeRequestBuilder

        return RealtimeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retention(self) -> RetentionRequestBuilder:
        """
        The retention property
        """
        from .retention.retention_request_builder import RetentionRequestBuilder

        return RetentionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def top(self) -> TopRequestBuilder:
        """
        The top property
        """
        from .top.top_request_builder import TopRequestBuilder

        return TopRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def videos(self) -> VideosRequestBuilder:
        """
        The videos property
        """
        from .videos.videos_request_builder import VideosRequestBuilder

        return VideosRequestBuilder(self.request_adapter, self.path_parameters)
    

