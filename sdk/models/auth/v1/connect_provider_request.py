from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .external_account_provider import ExternalAccountProvider
    from .user_request import UserRequest

@dataclass
class ConnectProviderRequest(Parsable):
    # The country_code property
    country_code: Optional[str] = None
    # The origin property
    origin: Optional[str] = None
    # The provider property
    provider: Optional[ExternalAccountProvider] = None
    # The token property
    token: Optional[str] = None
    # The user property
    user: Optional[UserRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectProviderRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectProviderRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectProviderRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .external_account_provider import ExternalAccountProvider
        from .user_request import UserRequest

        from .external_account_provider import ExternalAccountProvider
        from .user_request import UserRequest

        fields: dict[str, Callable[[Any], None]] = {
            "country_code": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(ExternalAccountProvider)),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(UserRequest)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("country_code", self.country_code)
        writer.write_str_value("origin", self.origin)
        writer.write_enum_value("provider", self.provider)
        writer.write_str_value("token", self.token)
        writer.write_object_value("user", self.user)
    

