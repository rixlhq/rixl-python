from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CreateVideoUploadBody(AdditionalDataHolder, Parsable):
    """
    Video upload details
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The image_format property
    image_format: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The video_quality property
    video_quality: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateVideoUploadBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateVideoUploadBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateVideoUploadBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "image_format": lambda n : setattr(self, 'image_format', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("image_format", self.image_format)
        writer.write_str_value("name", self.name)
        writer.write_str_value("video_quality", self.video_quality)
        writer.write_additional_data_value(self.additional_data)
    

