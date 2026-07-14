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
    from .......models.auth.v1.auto_join_setting import AutoJoinSetting
    from .auto_join_put_request_body import AutoJoinPutRequestBody

class AutoJoinRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /auth/v1/memberships/{org_-id}/domain/auto-join
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AutoJoinRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auth/v1/memberships/{org_%2Did}/domain/auto-join{?userId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AutoJoinRequestBuilderGetQueryParameters]] = None) -> Optional[AutoJoinSetting]:
        """
        GetDomainAutoJoin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AutoJoinSetting]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.auth.v1.auto_join_setting import AutoJoinSetting

        return await self.request_adapter.send_async(request_info, AutoJoinSetting, None)
    
    async def put(self,body: AutoJoinPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AutoJoinSetting]:
        """
        SetDomainAutoJoin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AutoJoinSetting]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.auth.v1.auto_join_setting import AutoJoinSetting

        return await self.request_adapter.send_async(request_info, AutoJoinSetting, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AutoJoinRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        GetDomainAutoJoin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: AutoJoinPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        SetDomainAutoJoin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AutoJoinRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AutoJoinRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AutoJoinRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AutoJoinRequestBuilderGetQueryParameters():
        """
        GetDomainAutoJoin
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "user_id":
                return "userId"
            return original_name
        
        user_id: Optional[str] = None

    
    @dataclass
    class AutoJoinRequestBuilderGetRequestConfiguration(RequestConfiguration[AutoJoinRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AutoJoinRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

