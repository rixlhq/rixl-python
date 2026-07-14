from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.common.v1.image_format import ImageFormat
    from .......models.common.v1.video_quality import VideoQuality

@dataclass
class UploadPostRequestBody(Parsable):
    # The imageFormat property
    image_format: Optional[ImageFormat] = None
    # The name property
    name: Optional[str] = None
    # The orgId property
    org_id: Optional[str] = None
    # The videoQuality property
    video_quality: Optional[VideoQuality] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UploadPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UploadPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UploadPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.common.v1.image_format import ImageFormat
        from .......models.common.v1.video_quality import VideoQuality

        from .......models.common.v1.image_format import ImageFormat
        from .......models.common.v1.video_quality import VideoQuality

        fields: dict[str, Callable[[Any], None]] = {
            "imageFormat": lambda n : setattr(self, 'image_format', n.get_enum_value(ImageFormat)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_enum_value("imageFormat", self.image_format)
        writer.write_str_value("name", self.name)
        writer.write_str_value("orgId", self.org_id)
        writer.write_enum_value("videoQuality", self.video_quality)
    

