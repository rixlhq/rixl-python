from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...analyticscommon.v1.media_type import MediaType
    from ...analyticscommon.v1.video_quality import VideoQuality
    from .content_view_event_page import ContentViewEvent_page
    from .content_view_event_view_type import ContentViewEvent_view_type
    from .segment import Segment

@dataclass
class ContentViewEvent(Parsable):
    # The audio_language property
    audio_language: Optional[str] = None
    # The content_id property
    content_id: Optional[str] = None
    # The content_type property
    content_type: Optional[MediaType] = None
    # The country property
    country: Optional[str] = None
    # The device_id property
    device_id: Optional[str] = None
    # The feed_id property
    feed_id: Optional[str] = None
    # The page property
    page: Optional[ContentViewEvent_page] = None
    # The post_id property
    post_id: Optional[str] = None
    # The quality property
    quality: Optional[VideoQuality] = None
    # The segments property
    segments: Optional[list[Segment]] = None
    # The subtitle_language property
    subtitle_language: Optional[str] = None
    # The video_position_ms property
    video_position_ms: Optional[datetime.timedelta] = None
    # The video_total_duration_ms property
    video_total_duration_ms: Optional[datetime.timedelta] = None
    # The view_type property
    view_type: Optional[ContentViewEvent_view_type] = None
    # The watch_duration_ms property
    watch_duration_ms: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentViewEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentViewEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentViewEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...analyticscommon.v1.media_type import MediaType
        from ...analyticscommon.v1.video_quality import VideoQuality
        from .content_view_event_page import ContentViewEvent_page
        from .content_view_event_view_type import ContentViewEvent_view_type
        from .segment import Segment

        from ...analyticscommon.v1.media_type import MediaType
        from ...analyticscommon.v1.video_quality import VideoQuality
        from .content_view_event_page import ContentViewEvent_page
        from .content_view_event_view_type import ContentViewEvent_view_type
        from .segment import Segment

        fields: dict[str, Callable[[Any], None]] = {
            "audio_language": lambda n : setattr(self, 'audio_language', n.get_str_value()),
            "content_id": lambda n : setattr(self, 'content_id', n.get_str_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_enum_value(MediaType)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "feed_id": lambda n : setattr(self, 'feed_id', n.get_str_value()),
            "page": lambda n : setattr(self, 'page', n.get_enum_value(ContentViewEvent_page)),
            "post_id": lambda n : setattr(self, 'post_id', n.get_str_value()),
            "quality": lambda n : setattr(self, 'quality', n.get_enum_value(VideoQuality)),
            "segments": lambda n : setattr(self, 'segments', n.get_collection_of_object_values(Segment)),
            "subtitle_language": lambda n : setattr(self, 'subtitle_language', n.get_str_value()),
            "video_position_ms": lambda n : setattr(self, 'video_position_ms', n.get_timedelta_value()),
            "video_total_duration_ms": lambda n : setattr(self, 'video_total_duration_ms', n.get_timedelta_value()),
            "view_type": lambda n : setattr(self, 'view_type', n.get_enum_value(ContentViewEvent_view_type)),
            "watch_duration_ms": lambda n : setattr(self, 'watch_duration_ms', n.get_timedelta_value()),
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
        writer.write_str_value("content_id", self.content_id)
        writer.write_enum_value("content_type", self.content_type)
        writer.write_str_value("country", self.country)
        writer.write_str_value("device_id", self.device_id)
        writer.write_str_value("feed_id", self.feed_id)
        writer.write_enum_value("page", self.page)
        writer.write_str_value("post_id", self.post_id)
        writer.write_enum_value("quality", self.quality)
        writer.write_collection_of_object_values("segments", self.segments)
        writer.write_str_value("subtitle_language", self.subtitle_language)
        writer.write_timedelta_value("video_position_ms", self.video_position_ms)
        writer.write_timedelta_value("video_total_duration_ms", self.video_total_duration_ms)
        writer.write_enum_value("view_type", self.view_type)
        writer.write_timedelta_value("watch_duration_ms", self.watch_duration_ms)
    

