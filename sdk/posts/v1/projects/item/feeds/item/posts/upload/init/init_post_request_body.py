from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..........models.common.v1.image_format import ImageFormat
    from ..........models.common.v1.media_type import MediaType
    from ..........models.common.v1.video_quality import VideoQuality

@dataclass
class InitPostRequestBody(Parsable):
    # The contentType property
    content_type: Optional[MediaType] = None
    # The creatorId property
    creator_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The fileName property
    file_name: Optional[str] = None
    # The format property
    format: Optional[str] = None
    # The imageFormat property
    image_format: Optional[ImageFormat] = None
    # The orgId property
    org_id: Optional[str] = None
    # The videoQuality property
    video_quality: Optional[VideoQuality] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InitPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InitPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InitPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..........models.common.v1.image_format import ImageFormat
        from ..........models.common.v1.media_type import MediaType
        from ..........models.common.v1.video_quality import VideoQuality

        from ..........models.common.v1.image_format import ImageFormat
        from ..........models.common.v1.media_type import MediaType
        from ..........models.common.v1.video_quality import VideoQuality

        fields: dict[str, Callable[[Any], None]] = {
            "contentType": lambda n : setattr(self, 'content_type', n.get_enum_value(MediaType)),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "imageFormat": lambda n : setattr(self, 'image_format', n.get_enum_value(ImageFormat)),
            "orgId": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "videoQuality": lambda n : setattr(self, 'video_quality', n.get_enum_value(VideoQuality)),
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
        writer.write_enum_value("contentType", self.content_type)
        writer.write_str_value("creatorId", self.creator_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("format", self.format)
        writer.write_enum_value("imageFormat", self.image_format)
        writer.write_str_value("orgId", self.org_id)
        writer.write_enum_value("videoQuality", self.video_quality)
    

