from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FeedStats(Parsable):
    # The avg_time_per_visit_ms property
    avg_time_per_visit_ms: Optional[float] = None
    # The feed_id property
    feed_id: Optional[str] = None
    # The total_watch_time_ms property
    total_watch_time_ms: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeedStats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeedStats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeedStats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_time_per_visit_ms": lambda n : setattr(self, 'avg_time_per_visit_ms', n.get_float_value()),
            "feed_id": lambda n : setattr(self, 'feed_id', n.get_str_value()),
            "total_watch_time_ms": lambda n : setattr(self, 'total_watch_time_ms', n.get_float_value()),
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
        writer.write_float_value("avg_time_per_visit_ms", self.avg_time_per_visit_ms)
        writer.write_str_value("feed_id", self.feed_id)
        writer.write_float_value("total_watch_time_ms", self.total_watch_time_ms)
    

