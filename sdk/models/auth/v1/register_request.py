from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RegisterRequest(Parsable):
    # The countryCode property
    country_code: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The password property
    password: Optional[str] = None
    # The subscribeToBlog property
    subscribe_to_blog: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RegisterRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RegisterRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RegisterRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "subscribeToBlog": lambda n : setattr(self, 'subscribe_to_blog', n.get_bool_value()),
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
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("email", self.email)
        writer.write_str_value("password", self.password)
        writer.write_bool_value("subscribeToBlog", self.subscribe_to_blog)
    

