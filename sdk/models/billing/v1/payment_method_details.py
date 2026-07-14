from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PaymentMethodDetails(Parsable):
    # The brand property
    brand: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The isDefault property
    is_default: Optional[bool] = None
    # The last4 property
    last4: Optional[str] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PaymentMethodDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PaymentMethodDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PaymentMethodDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "brand": lambda n : setattr(self, 'brand', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "last4": lambda n : setattr(self, 'last4', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("brand", self.brand)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("last4", self.last4)
        writer.write_str_value("type", self.type)
    

