from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_serialization_form.form_parse_node_factory import FormParseNodeFactory
from kiota_serialization_form.form_serialization_writer_factory import FormSerializationWriterFactory
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_multipart.multipart_serialization_writer_factory import MultipartSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .auth.auth_request_builder import AuthRequestBuilder
    from .billing.billing_request_builder import BillingRequestBuilder
    from .media.media_request_builder import MediaRequestBuilder
    from .organization.organization_request_builder import OrganizationRequestBuilder
    from .platform.platform_request_builder import PlatformRequestBuilder
    from .posts.posts_request_builder import PostsRequestBuilder
    from .projects.projects_request_builder import ProjectsRequestBuilder

class RixlClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new RixlClient and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_serializer(FormSerializationWriterFactory)
        register_default_serializer(MultipartSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        register_default_deserializer(FormParseNodeFactory)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://raw.githubusercontent.com"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        The analytics property
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def auth(self) -> AuthRequestBuilder:
        """
        The auth property
        """
        from .auth.auth_request_builder import AuthRequestBuilder

        return AuthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def billing(self) -> BillingRequestBuilder:
        """
        The billing property
        """
        from .billing.billing_request_builder import BillingRequestBuilder

        return BillingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def media(self) -> MediaRequestBuilder:
        """
        The media property
        """
        from .media.media_request_builder import MediaRequestBuilder

        return MediaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def organization(self) -> OrganizationRequestBuilder:
        """
        The organization property
        """
        from .organization.organization_request_builder import OrganizationRequestBuilder

        return OrganizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def platform(self) -> PlatformRequestBuilder:
        """
        The platform property
        """
        from .platform.platform_request_builder import PlatformRequestBuilder

        return PlatformRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def posts(self) -> PostsRequestBuilder:
        """
        The posts property
        """
        from .posts.posts_request_builder import PostsRequestBuilder

        return PostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> ProjectsRequestBuilder:
        """
        The projects property
        """
        from .projects.projects_request_builder import ProjectsRequestBuilder

        return ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    

