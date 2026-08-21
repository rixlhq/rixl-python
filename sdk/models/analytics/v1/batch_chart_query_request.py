from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chart_query_request import ChartQueryRequest

@dataclass
class BatchChartQueryRequest(Parsable):
    # The queries property
    queries: Optional[list[ChartQueryRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BatchChartQueryRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchChartQueryRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BatchChartQueryRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chart_query_request import ChartQueryRequest

        from .chart_query_request import ChartQueryRequest

        fields: dict[str, Callable[[Any], None]] = {
            "queries": lambda n : setattr(self, 'queries', n.get_collection_of_object_values(ChartQueryRequest)),
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
        writer.write_collection_of_object_values("queries", self.queries)
    

