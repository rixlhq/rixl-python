from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chart_row import ChartRow

@dataclass
class BatchChartQueryResult(Parsable):
    # The error property
    error: Optional[str] = None
    # The rows property
    rows: Optional[list[ChartRow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BatchChartQueryResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchChartQueryResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BatchChartQueryResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chart_row import ChartRow

        from .chart_row import ChartRow

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "rows": lambda n : setattr(self, 'rows', n.get_collection_of_object_values(ChartRow)),
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
        writer.write_str_value("error", self.error)
        writer.write_collection_of_object_values("rows", self.rows)
    

