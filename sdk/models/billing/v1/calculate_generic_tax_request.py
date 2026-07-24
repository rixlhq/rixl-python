from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_address import BillingAddress
    from .tax_line_item import TaxLineItem

@dataclass
class CalculateGenericTaxRequest(Parsable):
    # The billing_address property
    billing_address: Optional[BillingAddress] = None
    # The currency property
    currency: Optional[str] = None
    # The line_items property
    line_items: Optional[list[TaxLineItem]] = None
    # The org_id property
    org_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CalculateGenericTaxRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalculateGenericTaxRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CalculateGenericTaxRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_address import BillingAddress
        from .tax_line_item import TaxLineItem

        from .billing_address import BillingAddress
        from .tax_line_item import TaxLineItem

        fields: dict[str, Callable[[Any], None]] = {
            "billing_address": lambda n : setattr(self, 'billing_address', n.get_object_value(BillingAddress)),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "line_items": lambda n : setattr(self, 'line_items', n.get_collection_of_object_values(TaxLineItem)),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
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
        writer.write_str_value("currency", self.currency)
        writer.write_collection_of_object_values("line_items", self.line_items)
        writer.write_str_value("org_id", self.org_id)
    

