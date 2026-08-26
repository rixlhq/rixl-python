from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .chat.chat_request_builder import ChatRequestBuilder
    from .tickets.tickets_request_builder import TicketsRequestBuilder
    from .topics.topics_request_builder import TopicsRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /support/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/support/v1", path_parameters)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        The categories property
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chat(self) -> ChatRequestBuilder:
        """
        The chat property
        """
        from .chat.chat_request_builder import ChatRequestBuilder

        return ChatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tickets(self) -> TicketsRequestBuilder:
        """
        The tickets property
        """
        from .tickets.tickets_request_builder import TicketsRequestBuilder

        return TicketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def topics(self) -> TopicsRequestBuilder:
        """
        The topics property
        """
        from .topics.topics_request_builder import TopicsRequestBuilder

        return TopicsRequestBuilder(self.request_adapter, self.path_parameters)
    

