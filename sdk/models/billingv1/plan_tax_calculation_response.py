from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_address import BillingAddress

@dataclass
class PlanTaxCalculationResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The amount_total property
    amount_total: Optional[int] = None
    # The base_amount property
    base_amount: Optional[int] = None
    # The billing_address property
    billing_address: Optional[BillingAddress] = None
    # The billing_cycle property
    billing_cycle: Optional[str] = None
    # The calculated_at property
    calculated_at: Optional[str] = None
    # The calculation_id property
    calculation_id: Optional[str] = None
    # The currency property
    currency: Optional[str] = None
    # The plan_id property
    plan_id: Optional[str] = None
    # The plan_name property
    plan_name: Optional[str] = None
    # The tax_amount_exclusive property
    tax_amount_exclusive: Optional[int] = None
    # The tax_amount_inclusive property
    tax_amount_inclusive: Optional[int] = None
    # The tax_percentage property
    tax_percentage: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlanTaxCalculationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlanTaxCalculationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlanTaxCalculationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_address import BillingAddress

        from .billing_address import BillingAddress

        fields: dict[str, Callable[[Any], None]] = {
            "amount_total": lambda n : setattr(self, 'amount_total', n.get_int_value()),
            "base_amount": lambda n : setattr(self, 'base_amount', n.get_int_value()),
            "billing_address": lambda n : setattr(self, 'billing_address', n.get_object_value(BillingAddress)),
            "billing_cycle": lambda n : setattr(self, 'billing_cycle', n.get_str_value()),
            "calculated_at": lambda n : setattr(self, 'calculated_at', n.get_str_value()),
            "calculation_id": lambda n : setattr(self, 'calculation_id', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "plan_id": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "plan_name": lambda n : setattr(self, 'plan_name', n.get_str_value()),
            "tax_amount_exclusive": lambda n : setattr(self, 'tax_amount_exclusive', n.get_int_value()),
            "tax_amount_inclusive": lambda n : setattr(self, 'tax_amount_inclusive', n.get_int_value()),
            "tax_percentage": lambda n : setattr(self, 'tax_percentage', n.get_float_value()),
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
        writer.write_int_value("amount_total", self.amount_total)
        writer.write_int_value("base_amount", self.base_amount)
        writer.write_object_value("billing_address", self.billing_address)
        writer.write_str_value("billing_cycle", self.billing_cycle)
        writer.write_str_value("calculated_at", self.calculated_at)
        writer.write_str_value("calculation_id", self.calculation_id)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("plan_id", self.plan_id)
        writer.write_str_value("plan_name", self.plan_name)
        writer.write_int_value("tax_amount_exclusive", self.tax_amount_exclusive)
        writer.write_int_value("tax_amount_inclusive", self.tax_amount_inclusive)
        writer.write_float_value("tax_percentage", self.tax_percentage)
        writer.write_additional_data_value(self.additional_data)
    

