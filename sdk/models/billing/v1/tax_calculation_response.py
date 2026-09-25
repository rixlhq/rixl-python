from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TaxCalculationResponse(Parsable):
    # The amount_total property
    amount_total: Optional[int] = None
    # The calculation_id property
    calculation_id: Optional[str] = None
    # The currency property
    currency: Optional[str] = None
    # The tax_amount_exclusive property
    tax_amount_exclusive: Optional[int] = None
    # The tax_amount_inclusive property
    tax_amount_inclusive: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TaxCalculationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TaxCalculationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TaxCalculationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "amount_total": lambda n : setattr(self, 'amount_total', n.get_int_value()),
            "calculation_id": lambda n : setattr(self, 'calculation_id', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "tax_amount_exclusive": lambda n : setattr(self, 'tax_amount_exclusive', n.get_int_value()),
            "tax_amount_inclusive": lambda n : setattr(self, 'tax_amount_inclusive', n.get_int_value()),
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
        writer.write_str_value("calculation_id", self.calculation_id)
        writer.write_str_value("currency", self.currency)
        writer.write_int_value("tax_amount_exclusive", self.tax_amount_exclusive)
        writer.write_int_value("tax_amount_inclusive", self.tax_amount_inclusive)
    

