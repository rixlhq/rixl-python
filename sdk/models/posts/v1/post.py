from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...common.v1.media_type import MediaType
    from ...images.v1.image import Image
    from ...videos.v1.video import Video

@dataclass
class Post(Parsable):
    """
    At most one of `image`, `video` may be set.
    """
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    created_at: Optional[datetime.datetime] = None
    # The creator_id property
    creator_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The feed_id property
    feed_id: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The image property
    image: Optional[Image] = None
    # The type property
    type: Optional[MediaType] = None
    # The video property
    video: Optional[Video] = None
    
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
        from ...common.v1.media_type import MediaType
        from ...images.v1.image import Image
        from ...videos.v1.video import Video

        from ...common.v1.media_type import MediaType
        from ...images.v1.image import Image
        from ...videos.v1.video import Video

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "creator_id": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "feed_id": lambda n : setattr(self, 'feed_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_object_value(Image)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(MediaType)),
            "video": lambda n : setattr(self, 'video', n.get_object_value(Video)),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("creator_id", self.creator_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("feed_id", self.feed_id)
        writer.write_str_value("id", self.id)
        writer.write_object_value("image", self.image)
        writer.write_enum_value("type", self.type)
        writer.write_object_value("video", self.video)
    

