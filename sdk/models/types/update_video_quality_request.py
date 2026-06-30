from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..sqlc.video_quality import VideoQuality

@dataclass
class UpdateVideoQualityRequest(AdditionalDataHolder, Parsable):
    """
    New video quality setting
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The video_quality property
    video_quality: Optional[VideoQuality] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateVideoQualityRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateVideoQualityRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateVideoQualityRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..sqlc.video_quality import VideoQuality

        from ..sqlc.video_quality import VideoQuality

        fields: dict[str, Callable[[Any], None]] = {
            "video_quality": lambda n : setattr(self, 'video_quality', n.get_enum_value(VideoQuality)),
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
        writer.write_enum_value("video_quality", self.video_quality)
        writer.write_additional_data_value(self.additional_data)
    

