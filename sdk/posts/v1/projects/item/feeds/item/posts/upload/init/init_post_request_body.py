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
    # The content_type property
    content_type: Optional[MediaType] = None
    # The creator_id property
    creator_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The feed_id property
    feed_id: Optional[str] = None
    # The file_name property
    file_name: Optional[str] = None
    # The format property
    format: Optional[str] = None
    # The image_format property
    image_format: Optional[ImageFormat] = None
    # The org_id property
    org_id: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    # The video_quality property
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
            "content_type": lambda n : setattr(self, 'content_type', n.get_enum_value(MediaType)),
            "creator_id": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "feed_id": lambda n : setattr(self, 'feed_id', n.get_str_value()),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "image_format": lambda n : setattr(self, 'image_format', n.get_enum_value(ImageFormat)),
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
        writer.write_enum_value("content_type", self.content_type)
        writer.write_str_value("creator_id", self.creator_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("feed_id", self.feed_id)
        writer.write_str_value("file_name", self.file_name)
        writer.write_str_value("format", self.format)
        writer.write_enum_value("image_format", self.image_format)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("project_id", self.project_id)
        writer.write_enum_value("video_quality", self.video_quality)
    

