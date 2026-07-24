from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .payment_method import PaymentMethod

@dataclass
class ListPaymentMethodsResponse(Parsable):
    # The payment_methods property
    payment_methods: Optional[list[PaymentMethod]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListPaymentMethodsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListPaymentMethodsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListPaymentMethodsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .payment_method import PaymentMethod

        from .payment_method import PaymentMethod

        fields: dict[str, Callable[[Any], None]] = {
            "payment_methods": lambda n : setattr(self, 'payment_methods', n.get_collection_of_object_values(PaymentMethod)),
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
        writer.write_collection_of_object_values("payment_methods", self.payment_methods)
    

