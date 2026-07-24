from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BillingAddress(Parsable):
    # The city property
    city: Optional[str] = None
    # The country property
    country: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The line1 property
    line1: Optional[str] = None
    # The line2 property
    line2: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The phone property
    phone: Optional[str] = None
    # The postal_code property
    postal_code: Optional[str] = None
    # The state property
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BillingAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BillingAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BillingAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "line1": lambda n : setattr(self, 'line1', n.get_str_value()),
            "line2": lambda n : setattr(self, 'line2', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("email", self.email)
        writer.write_str_value("line1", self.line1)
        writer.write_str_value("line2", self.line2)
        writer.write_str_value("name", self.name)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("postal_code", self.postal_code)
        writer.write_str_value("state", self.state)
    

