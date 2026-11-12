from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_view_event import ContentViewEvent
    from .engagement_event import EngagementEvent
    from .error_event import ErrorEvent
    from .interaction_event import InteractionEvent
    from .session_start_event import SessionStartEvent

@dataclass
class AnalyticsEvent(Parsable):
    """
    At most one of `session_start`, `content_view`, `engagement`, `interaction`, `error` may be set.
    """
    # The content_view property
    content_view: Optional[ContentViewEvent] = None
    # The engagement property
    engagement: Optional[EngagementEvent] = None
    # The error property
    error: Optional[ErrorEvent] = None
    # The interaction property
    interaction: Optional[InteractionEvent] = None
    # The session_start property
    session_start: Optional[SessionStartEvent] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    timestamp: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyticsEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyticsEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyticsEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_view_event import ContentViewEvent
        from .engagement_event import EngagementEvent
        from .error_event import ErrorEvent
        from .interaction_event import InteractionEvent
        from .session_start_event import SessionStartEvent

        from .content_view_event import ContentViewEvent
        from .engagement_event import EngagementEvent
        from .error_event import ErrorEvent
        from .interaction_event import InteractionEvent
        from .session_start_event import SessionStartEvent

        fields: dict[str, Callable[[Any], None]] = {
            "content_view": lambda n : setattr(self, 'content_view', n.get_object_value(ContentViewEvent)),
            "engagement": lambda n : setattr(self, 'engagement', n.get_object_value(EngagementEvent)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(ErrorEvent)),
            "interaction": lambda n : setattr(self, 'interaction', n.get_object_value(InteractionEvent)),
            "session_start": lambda n : setattr(self, 'session_start', n.get_object_value(SessionStartEvent)),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
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
        writer.write_object_value("content_view", self.content_view)
        writer.write_object_value("engagement", self.engagement)
        writer.write_object_value("error", self.error)
        writer.write_object_value("interaction", self.interaction)
        writer.write_object_value("session_start", self.session_start)
        writer.write_datetime_value("timestamp", self.timestamp)
    

