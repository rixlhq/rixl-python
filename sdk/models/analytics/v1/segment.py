from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...analyticscommon.v1.video_quality import VideoQuality

@dataclass
class Segment(Parsable):
    # The audio_language property
    audio_language: Optional[str] = None
    # The chapter_title property
    chapter_title: Optional[str] = None
    # The end_ms property
    end_ms: Optional[datetime.timedelta] = None
    # enum.defined_only = true
    quality: Optional[VideoQuality] = None
    # The speed property
    speed: Optional[float] = None
    # The start_ms property
    start_ms: Optional[datetime.timedelta] = None
    # Unset fields inherit the value the view was opened with.
    subtitle_language: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Segment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Segment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Segment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...analyticscommon.v1.video_quality import VideoQuality

        from ...analyticscommon.v1.video_quality import VideoQuality

        fields: dict[str, Callable[[Any], None]] = {
            "audio_language": lambda n : setattr(self, 'audio_language', n.get_str_value()),
            "chapter_title": lambda n : setattr(self, 'chapter_title', n.get_str_value()),
            "end_ms": lambda n : setattr(self, 'end_ms', n.get_timedelta_value()),
            "quality": lambda n : setattr(self, 'quality', n.get_enum_value(VideoQuality)),
            "speed": lambda n : setattr(self, 'speed', n.get_float_value()),
            "start_ms": lambda n : setattr(self, 'start_ms', n.get_timedelta_value()),
            "subtitle_language": lambda n : setattr(self, 'subtitle_language', n.get_str_value()),
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
        writer.write_str_value("audio_language", self.audio_language)
        writer.write_str_value("chapter_title", self.chapter_title)
        writer.write_timedelta_value("end_ms", self.end_ms)
        writer.write_enum_value("quality", self.quality)
        writer.write_float_value("speed", self.speed)
        writer.write_timedelta_value("start_ms", self.start_ms)
        writer.write_str_value("subtitle_language", self.subtitle_language)
    

