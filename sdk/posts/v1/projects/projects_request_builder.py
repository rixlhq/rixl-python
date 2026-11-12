from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_project_item_request_builder import WithProject_ItemRequestBuilder

class ProjectsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /posts/v1/projects
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ProjectsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/posts/v1/projects", path_parameters)
    
    def by_project_id(self,project_id: str) -> WithProject_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.posts.v1.projects.item collection
        param project_id: Unique identifier of the item
        Returns: WithProject_ItemRequestBuilder
        """
        if project_id is None:
            raise TypeError("project_id cannot be null.")
        from .item.with_project_item_request_builder import WithProject_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["project_id"] = project_id
        return WithProject_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

