from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...common.v1.file import File
    from ...common.v1.visibility import Visibility
    from ...images.v1.image import Image

@dataclass
class Video(Parsable):
    # The bitrate property
    bitrate: Optional[int] = None
    # The codec property
    codec: Optional[str] = None
    # The duration property
    duration: Optional[datetime.timedelta] = None
    # The file property
    file: Optional[File] = None
    # The framerate property
    framerate: Optional[str] = None
    # The hdr property
    hdr: Optional[bool] = None
    # The height property
    height: Optional[int] = None
    # The id property
    id: Optional[str] = None
    # The poster property
    poster: Optional[Image] = None
    # The visibility property
    visibility: Optional[Visibility] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Video:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Video
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Video()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...common.v1.file import File
        from ...common.v1.visibility import Visibility
        from ...images.v1.image import Image

        from ...common.v1.file import File
        from ...common.v1.visibility import Visibility
        from ...images.v1.image import Image

        fields: dict[str, Callable[[Any], None]] = {
            "bitrate": lambda n : setattr(self, 'bitrate', n.get_int_value()),
            "codec": lambda n : setattr(self, 'codec', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(File)),
            "framerate": lambda n : setattr(self, 'framerate', n.get_str_value()),
            "hdr": lambda n : setattr(self, 'hdr', n.get_bool_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "poster": lambda n : setattr(self, 'poster', n.get_object_value(Image)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(Visibility)),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_int_value("bitrate", self.bitrate)
        writer.write_str_value("codec", self.codec)
        writer.write_timedelta_value("duration", self.duration)
        writer.write_object_value("file", self.file)
        writer.write_str_value("framerate", self.framerate)
        writer.write_bool_value("hdr", self.hdr)
        writer.write_int_value("height", self.height)
        writer.write_str_value("id", self.id)
        writer.write_object_value("poster", self.poster)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_int_value("width", self.width)
    

