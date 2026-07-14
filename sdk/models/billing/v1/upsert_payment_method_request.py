from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UpsertPaymentMethodRequest(Parsable):
    # The orgId property
    org_id: Optional[str] = None
    # The paymentMethodId property
    payment_method_id: Optional[str] = None
    # The setAsDefault property
    set_as_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpsertPaymentMethodRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpsertPaymentMethodRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpsertPaymentMethodRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "orgId": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "paymentMethodId": lambda n : setattr(self, 'payment_method_id', n.get_str_value()),
            "setAsDefault": lambda n : setattr(self, 'set_as_default', n.get_bool_value()),
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
        writer.write_str_value("orgId", self.org_id)
        writer.write_str_value("paymentMethodId", self.payment_method_id)
        writer.write_bool_value("setAsDefault", self.set_as_default)
    

