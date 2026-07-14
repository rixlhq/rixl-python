from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_address import BillingAddress

@dataclass
class CreateSubscriptionRequest(Parsable):
    # The billingAddress property
    billing_address: Optional[BillingAddress] = None
    # The orgId property
    org_id: Optional[str] = None
    # The paymentMethodId property
    payment_method_id: Optional[str] = None
    # The stripePriceId property
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
            "billingAddress": lambda n : setattr(self, 'billing_address', n.get_object_value(BillingAddress)),
            "orgId": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "paymentMethodId": lambda n : setattr(self, 'payment_method_id', n.get_str_value()),
            "stripePriceId": lambda n : setattr(self, 'stripe_price_id', n.get_str_value()),
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
        writer.write_object_value("billingAddress", self.billing_address)
        writer.write_str_value("orgId", self.org_id)
        writer.write_str_value("paymentMethodId", self.payment_method_id)
        writer.write_str_value("stripePriceId", self.stripe_price_id)
    

