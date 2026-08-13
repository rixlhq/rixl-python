from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chart_row_dimensions import ChartRow_dimensions

@dataclass
class ChartRow(Parsable):
    # The dimensions property
    dimensions: Optional[ChartRow_dimensions] = None
    # The timestamp property
    timestamp: Optional[str] = None
    # The value property
    value: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChartRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChartRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChartRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chart_row_dimensions import ChartRow_dimensions

        from .chart_row_dimensions import ChartRow_dimensions

        fields: dict[str, Callable[[Any], None]] = {
            "dimensions": lambda n : setattr(self, 'dimensions', n.get_object_value(ChartRow_dimensions)),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_float_value()),
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
        writer.write_object_value("dimensions", self.dimensions)
        writer.write_str_value("timestamp", self.timestamp)
        writer.write_float_value("value", self.value)
    

