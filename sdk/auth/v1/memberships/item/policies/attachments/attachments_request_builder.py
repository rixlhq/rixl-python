from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_attachment_item_request_builder import WithAttachment_ItemRequestBuilder

class AttachmentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{org_-id}/policies/attachments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AttachmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{org_%2Did}/policies/attachments", path_parameters)
    
    def by_attachment_id(self,attachment_id: str) -> WithAttachment_ItemRequestBuilder:
        """
        Gets an item from the rixl_sdk.auth.v1.memberships.item.policies.attachments.item collection
        param attachment_id: Unique identifier of the item
        Returns: WithAttachment_ItemRequestBuilder
        """
        if attachment_id is None:
            raise TypeError("attachment_id cannot be null.")
        from .item.with_attachment_item_request_builder import WithAttachment_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attachment_id"] = attachment_id
        return WithAttachment_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

