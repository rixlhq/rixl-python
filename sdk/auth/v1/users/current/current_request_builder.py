from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.authv1.user_info import UserInfo
    from .emails.emails_request_builder import EmailsRequestBuilder
    from .name.name_request_builder import NameRequestBuilder
    from .passkeys.passkeys_request_builder import PasskeysRequestBuilder
    from .totp.totp_request_builder import TotpRequestBuilder
    from .username.username_request_builder import UsernameRequestBuilder

class CurrentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/users/current
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CurrentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/users/current", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UserInfo]:
        """
        Returns the profile information of the authenticated user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserInfo]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.authv1.user_info import UserInfo

        return await self.request_adapter.send_async(request_info, UserInfo, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the profile information of the authenticated user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CurrentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CurrentRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CurrentRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def emails(self) -> EmailsRequestBuilder:
        """
        The emails property
        """
        from .emails.emails_request_builder import EmailsRequestBuilder

        return EmailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def name(self) -> NameRequestBuilder:
        """
        The name property
        """
        from .name.name_request_builder import NameRequestBuilder

        return NameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passkeys(self) -> PasskeysRequestBuilder:
        """
        The passkeys property
        """
        from .passkeys.passkeys_request_builder import PasskeysRequestBuilder

        return PasskeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def totp(self) -> TotpRequestBuilder:
        """
        The totp property
        """
        from .totp.totp_request_builder import TotpRequestBuilder

        return TotpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def username(self) -> UsernameRequestBuilder:
        """
        The username property
        """
        from .username.username_request_builder import UsernameRequestBuilder

        return UsernameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CurrentRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

