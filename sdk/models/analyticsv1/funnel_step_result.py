from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FunnelStepResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The conversion_rate property
    conversion_rate: Optional[float] = None
    # The dropoff_rate property
    dropoff_rate: Optional[float] = None
    # The step_name property
    step_name: Optional[str] = None
    # The user_count property
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FunnelStepResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FunnelStepResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FunnelStepResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "conversion_rate": lambda n : setattr(self, 'conversion_rate', n.get_float_value()),
            "dropoff_rate": lambda n : setattr(self, 'dropoff_rate', n.get_float_value()),
            "step_name": lambda n : setattr(self, 'step_name', n.get_str_value()),
            "user_count": lambda n : setattr(self, 'user_count', n.get_int_value()),
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
        writer.write_float_value("conversion_rate", self.conversion_rate)
        writer.write_float_value("dropoff_rate", self.dropoff_rate)
        writer.write_str_value("step_name", self.step_name)
        writer.write_int_value("user_count", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

