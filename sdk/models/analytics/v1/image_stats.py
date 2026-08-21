from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ImageStats(Parsable):
    # Dwell time; images have no playback.
    avg_view_duration_ms: Optional[float] = None
    # The image_id property
    image_id: Optional[str] = None
    # The total_view_duration_ms property
    total_view_duration_ms: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImageStats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImageStats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImageStats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_view_duration_ms": lambda n : setattr(self, 'avg_view_duration_ms', n.get_float_value()),
            "image_id": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "total_view_duration_ms": lambda n : setattr(self, 'total_view_duration_ms', n.get_float_value()),
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
        writer.write_float_value("avg_view_duration_ms", self.avg_view_duration_ms)
        writer.write_str_value("image_id", self.image_id)
        writer.write_float_value("total_view_duration_ms", self.total_view_duration_ms)
    

