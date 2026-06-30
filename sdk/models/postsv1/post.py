from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .post_image import PostImage
    from .post_video import PostVideo

@dataclass
class Post(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[str] = None
    # The creator_id property
    creator_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The feed_id property
    feed_id: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The image property
    image: Optional[PostImage] = None
    # The image_id property
    image_id: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The video property
    video: Optional[PostVideo] = None
    # The video_id property
    video_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Post:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Post
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Post()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .post_image import PostImage
        from .post_video import PostVideo

        from .post_image import PostImage
        from .post_video import PostVideo

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "creator_id": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "feed_id": lambda n : setattr(self, 'feed_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_object_value(PostImage)),
            "image_id": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "video": lambda n : setattr(self, 'video', n.get_object_value(PostVideo)),
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
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("creator_id", self.creator_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("feed_id", self.feed_id)
        writer.write_str_value("id", self.id)
        writer.write_object_value("image", self.image)
        writer.write_str_value("image_id", self.image_id)
        writer.write_str_value("type", self.type)
        writer.write_object_value("video", self.video)
        writer.write_str_value("video_id", self.video_id)
        writer.write_additional_data_value(self.additional_data)
    

