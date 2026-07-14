from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .refresh.refresh_request_builder import RefreshRequestBuilder
    from .token.token_request_builder import TokenRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /platform/auth/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/platform/auth/v1", path_parameters)
    
    @property
    def refresh(self) -> RefreshRequestBuilder:
        """
        The refresh property
        """
        from .refresh.refresh_request_builder import RefreshRequestBuilder

        return RefreshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token(self) -> TokenRequestBuilder:
        """
        The token property
        """
        from .token.token_request_builder import TokenRequestBuilder

        return TokenRequestBuilder(self.request_adapter, self.path_parameters)
    

