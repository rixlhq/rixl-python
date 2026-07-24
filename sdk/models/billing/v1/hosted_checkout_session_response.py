from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class HostedCheckoutSessionResponse(Parsable):
    # The amount property
    amount: Optional[float] = None
    # The currency property
    currency: Optional[str] = None
    # The session_id property
    session_id: Optional[str] = None
    # The session_url property
    session_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HostedCheckoutSessionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostedCheckoutSessionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HostedCheckoutSessionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "session_id": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "session_url": lambda n : setattr(self, 'session_url', n.get_str_value()),
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
        writer.write_float_value("amount", self.amount)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("session_id", self.session_id)
        writer.write_str_value("session_url", self.session_url)
    

