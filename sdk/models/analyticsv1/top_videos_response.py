from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .video_stats import VideoStats

@dataclass
class TopVideosResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The videos property
    videos: Optional[list[VideoStats]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TopVideosResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TopVideosResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TopVideosResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .video_stats import VideoStats

        from .video_stats import VideoStats

        fields: dict[str, Callable[[Any], None]] = {
            "videos": lambda n : setattr(self, 'videos', n.get_collection_of_object_values(VideoStats)),
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
        writer.write_collection_of_object_values("videos", self.videos)
        writer.write_additional_data_value(self.additional_data)
    

