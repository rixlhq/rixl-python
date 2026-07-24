from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_address import BillingAddress

@dataclass
class CreateSubscriptionRequest(Parsable):
    # The billing_address property
    billing_address: Optional[BillingAddress] = None
    # The org_id property
    org_id: Optional[str] = None
    # The payment_method_id property
    payment_method_id: Optional[str] = None
    # The stripe_price_id property
    stripe_price_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateSubscriptionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateSubscriptionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateSubscriptionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_address import BillingAddress

        from .billing_address import BillingAddress

        fields: dict[str, Callable[[Any], None]] = {
            "billing_address": lambda n : setattr(self, 'billing_address', n.get_object_value(BillingAddress)),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "payment_method_id": lambda n : setattr(self, 'payment_method_id', n.get_str_value()),
            "stripe_price_id": lambda n : setattr(self, 'stripe_price_id', n.get_str_value()),
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
        writer.write_object_value("billing_address", self.billing_address)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("payment_method_id", self.payment_method_id)
        writer.write_str_value("stripe_price_id", self.stripe_price_id)
    

