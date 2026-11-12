from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_token_item_request_builder import WithTokenItemRequestBuilder

class InvitationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/invitations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvitationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/invitations", path_parameters)
    
    def by_token(self,token: str) -> WithTokenItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.invitations.item collection
        param token: Unique identifier of the item
        Returns: WithTokenItemRequestBuilder
        """
        if token is None:
            raise TypeError("token cannot be null.")
        from .item.with_token_item_request_builder import WithTokenItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["token"] = token
        return WithTokenItemRequestBuilder(self.request_adapter, url_tpl_params)
    

