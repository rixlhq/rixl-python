from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PaymentMethod(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[str] = None
    # The details property
    details: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The is_default property
    is_default: Optional[bool] = None
    # The org_id property
    org_id: Optional[str] = None
    # The provider property
    provider: Optional[str] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PaymentMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PaymentMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PaymentMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
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
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("details", self.details)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("is_default", self.is_default)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

