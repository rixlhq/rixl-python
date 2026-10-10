from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_language_code_item_request_builder import WithLanguage_codeItemRequestBuilder

class LanguageRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/projects/{project_id}/videos/{video_id}/subtitles/language
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LanguageRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/projects/{project_id}/videos/{video_id}/subtitles/language", path_parameters)
    
    def by_language_code(self,language_code: str) -> WithLanguage_codeItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.v1.projects.item.videos.item.subtitles.language.item collection
        param language_code: Unique identifier of the item
        Returns: WithLanguage_codeItemRequestBuilder
        """
        if language_code is None:
            raise TypeError("language_code cannot be null.")
        from .item.with_language_code_item_request_builder import WithLanguage_codeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["language_code"] = language_code
        return WithLanguage_codeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

