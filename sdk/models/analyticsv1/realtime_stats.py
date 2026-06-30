from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .country_count import CountryCount
    from .event_count import EventCount
    from .recent_event import RecentEvent

@dataclass
class RealtimeStats(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active_users property
    active_users: Optional[int] = None
    # The events_per_minute property
    events_per_minute: Optional[int] = None
    # The recent_events property
    recent_events: Optional[list[RecentEvent]] = None
    # The timestamp property
    timestamp: Optional[str] = None
    # The top_countries property
    top_countries: Optional[list[CountryCount]] = None
    # The top_events property
    top_events: Optional[list[EventCount]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RealtimeStats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RealtimeStats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RealtimeStats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .country_count import CountryCount
        from .event_count import EventCount
        from .recent_event import RecentEvent

        from .country_count import CountryCount
        from .event_count import EventCount
        from .recent_event import RecentEvent

        fields: dict[str, Callable[[Any], None]] = {
            "active_users": lambda n : setattr(self, 'active_users', n.get_int_value()),
            "events_per_minute": lambda n : setattr(self, 'events_per_minute', n.get_int_value()),
            "recent_events": lambda n : setattr(self, 'recent_events', n.get_collection_of_object_values(RecentEvent)),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_str_value()),
            "top_countries": lambda n : setattr(self, 'top_countries', n.get_collection_of_object_values(CountryCount)),
            "top_events": lambda n : setattr(self, 'top_events', n.get_collection_of_object_values(EventCount)),
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
        writer.write_int_value("active_users", self.active_users)
        writer.write_int_value("events_per_minute", self.events_per_minute)
        writer.write_collection_of_object_values("recent_events", self.recent_events)
        writer.write_str_value("timestamp", self.timestamp)
        writer.write_collection_of_object_values("top_countries", self.top_countries)
        writer.write_collection_of_object_values("top_events", self.top_events)
        writer.write_additional_data_value(self.additional_data)
    

