from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CreateCheckoutSessionRequest(Parsable):
    # The cancelUrl property
    cancel_url: Optional[str] = None
    # The orgId property
    org_id: Optional[str] = None
    # The stripePriceId property
    stripe_price_id: Optional[str] = None
    # The successUrl property
    success_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateCheckoutSessionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateCheckoutSessionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateCheckoutSessionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cancelUrl": lambda n : setattr(self, 'cancel_url', n.get_str_value()),
            "orgId": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "stripePriceId": lambda n : setattr(self, 'stripe_price_id', n.get_str_value()),
            "successUrl": lambda n : setattr(self, 'success_url', n.get_str_value()),
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
        writer.write_str_value("cancelUrl", self.cancel_url)
        writer.write_str_value("orgId", self.org_id)
        writer.write_str_value("stripePriceId", self.stripe_price_id)
        writer.write_str_value("successUrl", self.success_url)
    

