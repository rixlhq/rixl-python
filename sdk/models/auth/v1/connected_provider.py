from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .external_account_provider import ExternalAccountProvider

@dataclass
class ConnectedProvider(Parsable):
    # The emailAddress property
    email_address: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The imageUrl property
    image_url: Optional[str] = None
    # The lastName property
    last_name: Optional[str] = None
    # The provider property
    provider: Optional[ExternalAccountProvider] = None
    # The username property
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectedProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectedProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectedProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .external_account_provider import ExternalAccountProvider

        from .external_account_provider import ExternalAccountProvider

        fields: dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "imageUrl": lambda n : setattr(self, 'image_url', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(ExternalAccountProvider)),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
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
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("imageUrl", self.image_url)
        writer.write_str_value("lastName", self.last_name)
        writer.write_enum_value("provider", self.provider)
        writer.write_str_value("username", self.username)
    

