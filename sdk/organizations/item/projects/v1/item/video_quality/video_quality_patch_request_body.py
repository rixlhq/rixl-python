from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.common.v1.video_quality import VideoQuality

@dataclass
class VideoQualityPatchRequestBody(Parsable):
    # The org_id property
    org_id: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    # The video_quality property
    video_quality: Optional[VideoQuality] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VideoQualityPatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VideoQualityPatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VideoQualityPatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.common.v1.video_quality import VideoQuality

        from .......models.common.v1.video_quality import VideoQuality

        fields: dict[str, Callable[[Any], None]] = {
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
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
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("project_id", self.project_id)
        writer.write_enum_value("video_quality", self.video_quality)
    

