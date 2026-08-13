from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chart_filter import ChartFilter

@dataclass
class ChartQueryRequest(Parsable):
    # The dataset property
    dataset: Optional[str] = None
    # The filters property
    filters: Optional[list[ChartFilter]] = None
    # The group_by property
    group_by: Optional[list[str]] = None
    # The interval property
    interval: Optional[str] = None
    # The limit property
    limit: Optional[int] = None
    # The metric property
    metric: Optional[str] = None
    # The time_end property
    time_end: Optional[str] = None
    # The time_start property
    time_start: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChartQueryRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChartQueryRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChartQueryRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chart_filter import ChartFilter

        from .chart_filter import ChartFilter

        fields: dict[str, Callable[[Any], None]] = {
            "dataset": lambda n : setattr(self, 'dataset', n.get_str_value()),
            "filters": lambda n : setattr(self, 'filters', n.get_collection_of_object_values(ChartFilter)),
            "group_by": lambda n : setattr(self, 'group_by', n.get_collection_of_primitive_values(str)),
            "interval": lambda n : setattr(self, 'interval', n.get_str_value()),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "metric": lambda n : setattr(self, 'metric', n.get_str_value()),
            "time_end": lambda n : setattr(self, 'time_end', n.get_str_value()),
            "time_start": lambda n : setattr(self, 'time_start', n.get_str_value()),
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
        writer.write_str_value("dataset", self.dataset)
        writer.write_collection_of_object_values("filters", self.filters)
        writer.write_collection_of_primitive_values("group_by", self.group_by)
        writer.write_str_value("interval", self.interval)
        writer.write_int_value("limit", self.limit)
        writer.write_str_value("metric", self.metric)
        writer.write_str_value("time_end", self.time_end)
        writer.write_str_value("time_start", self.time_start)
    

