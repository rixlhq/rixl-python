from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hot_segment import HotSegment

@dataclass
class HotSegmentsResponse(Parsable):
    # The segments property
    segments: Optional[list[HotSegment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HotSegmentsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HotSegmentsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HotSegmentsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hot_segment import HotSegment

        from .hot_segment import HotSegment

        fields: dict[str, Callable[[Any], None]] = {
            "segments": lambda n : setattr(self, 'segments', n.get_collection_of_object_values(HotSegment)),
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
        writer.write_collection_of_object_values("segments", self.segments)
    

