from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class VideoStats(Parsable):
    # The avg_watch_time_ms property
    avg_watch_time_ms: Optional[float] = None
    # The completion_rate property
    completion_rate: Optional[float] = None
    # The total_watch_time_ms property
    total_watch_time_ms: Optional[float] = None
    # The video_id property
    video_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VideoStats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VideoStats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VideoStats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_watch_time_ms": lambda n : setattr(self, 'avg_watch_time_ms', n.get_float_value()),
            "completion_rate": lambda n : setattr(self, 'completion_rate', n.get_float_value()),
            "total_watch_time_ms": lambda n : setattr(self, 'total_watch_time_ms', n.get_float_value()),
            "video_id": lambda n : setattr(self, 'video_id', n.get_str_value()),
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
        writer.write_float_value("avg_watch_time_ms", self.avg_watch_time_ms)
        writer.write_float_value("completion_rate", self.completion_rate)
        writer.write_float_value("total_watch_time_ms", self.total_watch_time_ms)
        writer.write_str_value("video_id", self.video_id)
    

