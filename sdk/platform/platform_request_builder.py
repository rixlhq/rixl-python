from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .auth.auth_request_builder import AuthRequestBuilder
    from .clientauth.clientauth_request_builder import ClientauthRequestBuilder

class PlatformRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /platform
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlatformRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/platform", path_parameters)
    
    @property
    def auth(self) -> AuthRequestBuilder:
        """
        The auth property
        """
        from .auth.auth_request_builder import AuthRequestBuilder

        return AuthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clientauth(self) -> ClientauthRequestBuilder:
        """
        The clientauth property
        """
        from .clientauth.clientauth_request_builder import ClientauthRequestBuilder

        return ClientauthRequestBuilder(self.request_adapter, self.path_parameters)
    

