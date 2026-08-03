from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .video import Video

@dataclass
class UpdateVideoVisibilityResponse(Parsable):
    # The video property
    video: Optional[Video] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateVideoVisibilityResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateVideoVisibilityResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateVideoVisibilityResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .video import Video

        from .video import Video

        fields: dict[str, Callable[[Any], None]] = {
            "video": lambda n : setattr(self, 'video', n.get_object_value(Video)),
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
        writer.write_object_value("video", self.video)
    

