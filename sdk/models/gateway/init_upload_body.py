from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .init_upload_body_content_type import InitUploadBody_content_type

@dataclass
class InitUploadBody(AdditionalDataHolder, Parsable):
    """
    Upload initialization request
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The content_type property
    content_type: Optional[InitUploadBody_content_type] = None
    # The creator_id property
    creator_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The file_name property
    file_name: Optional[str] = None
    # The format property
    format: Optional[str] = None
    # The image_format property
    image_format: Optional[str] = None
    # The video_quality property
    video_quality: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InitUploadBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InitUploadBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InitUploadBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .init_upload_body_content_type import InitUploadBody_content_type

        from .init_upload_body_content_type import InitUploadBody_content_type

        fields: dict[str, Callable[[Any], None]] = {
            "content_type": lambda n : setattr(self, 'content_type', n.get_enum_value(InitUploadBody_content_type)),
            "creator_id": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "image_format": lambda n : setattr(self, 'image_format', n.get_str_value()),
            "video_quality": lambda n : setattr(self, 'video_quality', n.get_str_value()),
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
        writer.write_str_value("file_name", self.file_name)
        writer.write_str_value("format", self.format)
        writer.write_str_value("image_format", self.image_format)
        writer.write_str_value("video_quality", self.video_quality)
        writer.write_additional_data_value(self.additional_data)
    

