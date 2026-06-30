from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_lang_item_request_builder import WithLangItemRequestBuilder

class LanguageRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /media/v1/projects/{projectId}/videos/{videoId}/subtitles/language
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LanguageRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/media/v1/projects/{projectId}/videos/{videoId}/subtitles/language", path_parameters)
    
    def by_lang(self,lang: str) -> WithLangItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.media.v1.projects.item.videos.item.subtitles.language.item collection
        param lang: Language code
        Returns: WithLangItemRequestBuilder
        """
        if lang is None:
            raise TypeError("lang cannot be null.")
        from .item.with_lang_item_request_builder import WithLangItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["lang"] = lang
        return WithLangItemRequestBuilder(self.request_adapter, url_tpl_params)
    

