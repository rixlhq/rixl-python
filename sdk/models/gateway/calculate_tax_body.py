from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_address_body import BillingAddressBody
    from .calculate_tax_body_metadata import CalculateTaxBody_metadata
    from .tax_line_item_body import TaxLineItemBody

@dataclass
class CalculateTaxBody(AdditionalDataHolder, Parsable):
    """
    Tax calculation request
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The amount property
    amount: Optional[float] = None
    # The billing_address property
    billing_address: Optional[BillingAddressBody] = None
    # The billing_cycle property
    billing_cycle: Optional[str] = None
    # The currency property
    currency: Optional[str] = None
    # The interval_count property
    interval_count: Optional[int] = None
    # The line_items property
    line_items: Optional[list[TaxLineItemBody]] = None
    # The metadata property
    metadata: Optional[CalculateTaxBody_metadata] = None
    # The plan_id property
    plan_id: Optional[str] = None
    # The plan_name property
    plan_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CalculateTaxBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalculateTaxBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CalculateTaxBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_address_body import BillingAddressBody
        from .calculate_tax_body_metadata import CalculateTaxBody_metadata
        from .tax_line_item_body import TaxLineItemBody

        from .billing_address_body import BillingAddressBody
        from .calculate_tax_body_metadata import CalculateTaxBody_metadata
        from .tax_line_item_body import TaxLineItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "billing_address": lambda n : setattr(self, 'billing_address', n.get_object_value(BillingAddressBody)),
            "billing_cycle": lambda n : setattr(self, 'billing_cycle', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "interval_count": lambda n : setattr(self, 'interval_count', n.get_int_value()),
            "line_items": lambda n : setattr(self, 'line_items', n.get_collection_of_object_values(TaxLineItemBody)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(CalculateTaxBody_metadata)),
            "plan_id": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "plan_name": lambda n : setattr(self, 'plan_name', n.get_str_value()),
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
        writer.write_object_value("billing_address", self.billing_address)
        writer.write_str_value("billing_cycle", self.billing_cycle)
        writer.write_str_value("currency", self.currency)
        writer.write_int_value("interval_count", self.interval_count)
        writer.write_collection_of_object_values("line_items", self.line_items)
        writer.write_object_value("metadata", self.metadata)
        writer.write_str_value("plan_id", self.plan_id)
        writer.write_str_value("plan_name", self.plan_name)
        writer.write_additional_data_value(self.additional_data)
    

