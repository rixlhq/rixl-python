from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .post_stats_views_by_page import PostStats_views_by_page

@dataclass
class PostStats(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The avg_watch_time_ms property
    avg_watch_time_ms: Optional[float] = None
    # The completion_rate property
    completion_rate: Optional[float] = None
    # The completions property
    completions: Optional[int] = None
    # The content_type property
    content_type: Optional[str] = None
    # The feed_id property
    feed_id: Optional[str] = None
    # The post_id property
    post_id: Optional[str] = None
    # The starts property
    starts: Optional[int] = None
    # The total_views property
    total_views: Optional[int] = None
    # The total_watch_time_ms property
    total_watch_time_ms: Optional[int] = None
    # The unique_viewers property
    unique_viewers: Optional[int] = None
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
        from .post_stats_views_by_page import PostStats_views_by_page

        from .post_stats_views_by_page import PostStats_views_by_page

        fields: dict[str, Callable[[Any], None]] = {
            "avg_watch_time_ms": lambda n : setattr(self, 'avg_watch_time_ms', n.get_float_value()),
            "completion_rate": lambda n : setattr(self, 'completion_rate', n.get_float_value()),
            "completions": lambda n : setattr(self, 'completions', n.get_int_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "feed_id": lambda n : setattr(self, 'feed_id', n.get_str_value()),
            "post_id": lambda n : setattr(self, 'post_id', n.get_str_value()),
            "starts": lambda n : setattr(self, 'starts', n.get_int_value()),
            "total_views": lambda n : setattr(self, 'total_views', n.get_int_value()),
            "total_watch_time_ms": lambda n : setattr(self, 'total_watch_time_ms', n.get_int_value()),
            "unique_viewers": lambda n : setattr(self, 'unique_viewers', n.get_int_value()),
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
        writer.write_int_value("completions", self.completions)
        writer.write_str_value("content_type", self.content_type)
        writer.write_str_value("feed_id", self.feed_id)
        writer.write_str_value("post_id", self.post_id)
        writer.write_int_value("starts", self.starts)
        writer.write_int_value("total_views", self.total_views)
        writer.write_int_value("total_watch_time_ms", self.total_watch_time_ms)
        writer.write_int_value("unique_viewers", self.unique_viewers)
        writer.write_object_value("views_by_page", self.views_by_page)
        writer.write_additional_data_value(self.additional_data)
    

