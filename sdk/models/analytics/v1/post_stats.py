from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...analyticscommon.v1.media_type import MediaType
    from .post_stats_views_by_page import PostStats_views_by_page

@dataclass
class PostStats(Parsable):
    # The avg_watch_time_ms property
    avg_watch_time_ms: Optional[float] = None
    # The completion_rate property
    completion_rate: Optional[float] = None
    # The content_type property
    content_type: Optional[MediaType] = None
    # The feed_id property
    feed_id: Optional[str] = None
    # The post_id property
    post_id: Optional[str] = None
    # The views_by_page property
    views_by_page: Optional[PostStats_views_by_page] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PostStats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PostStats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PostStats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...analyticscommon.v1.media_type import MediaType
        from .post_stats_views_by_page import PostStats_views_by_page

        from ...analyticscommon.v1.media_type import MediaType
        from .post_stats_views_by_page import PostStats_views_by_page

        fields: dict[str, Callable[[Any], None]] = {
            "avg_watch_time_ms": lambda n : setattr(self, 'avg_watch_time_ms', n.get_float_value()),
            "completion_rate": lambda n : setattr(self, 'completion_rate', n.get_float_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_enum_value(MediaType)),
            "feed_id": lambda n : setattr(self, 'feed_id', n.get_str_value()),
            "post_id": lambda n : setattr(self, 'post_id', n.get_str_value()),
            "views_by_page": lambda n : setattr(self, 'views_by_page', n.get_object_value(PostStats_views_by_page)),
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
        writer.write_float_value("avg_watch_time_ms", self.avg_watch_time_ms)
        writer.write_float_value("completion_rate", self.completion_rate)
        writer.write_enum_value("content_type", self.content_type)
        writer.write_str_value("feed_id", self.feed_id)
        writer.write_str_value("post_id", self.post_id)
        writer.write_object_value("views_by_page", self.views_by_page)
    

