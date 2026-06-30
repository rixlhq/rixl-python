from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_post_body_type import CreatePostBody_type

@dataclass
class CreatePostBody(AdditionalDataHolder, Parsable):
    """
    Post to create
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The creator_id property
    creator_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The image_id property
    image_id: Optional[str] = None
    # The type property
    type: Optional[CreatePostBody_type] = None
    # The video_id property
    video_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreatePostBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreatePostBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreatePostBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .create_post_body_type import CreatePostBody_type

        from .create_post_body_type import CreatePostBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "creator_id": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "image_id": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CreatePostBody_type)),
            "video_id": lambda n : setattr(self, 'video_id', n.get_str_value()),
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
        writer.write_str_value("creator_id", self.creator_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("image_id", self.image_id)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("video_id", self.video_id)
        writer.write_additional_data_value(self.additional_data)
    

