from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_event import AnalyticsEvent

@dataclass
class TrackEventsRequest(Parsable):
    # The browser property
    browser: Optional[str] = None
    # The city property
    city: Optional[str] = None
    # The country property
    country: Optional[str] = None
    # The device property
    device: Optional[str] = None
    # The events property
    events: Optional[list[AnalyticsEvent]] = None
    # The language property
    language: Optional[str] = None
    # The os property
    os: Optional[str] = None
    # The os_version property
    os_version: Optional[str] = None
    # Project the events belong to (Organization > Project > Videos/Images/Posts/Feeds). Sent alongside the other envelope-level context because a client session is scoped to one project. org_id is still derived server-side from the credential and is never taken from the body, so a wrong project_id can only mis-attribute within the caller's own organization.
    project_id: Optional[str] = None
    # The region property
    region: Optional[str] = None
    # The user_id property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrackEventsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrackEventsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrackEventsRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_event import AnalyticsEvent

        from .analytics_event import AnalyticsEvent

        fields: dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "device": lambda n : setattr(self, 'device', n.get_str_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(AnalyticsEvent)),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("device", self.device)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("language", self.language)
        writer.write_str_value("os", self.os)
        writer.write_str_value("os_version", self.os_version)
        writer.write_str_value("project_id", self.project_id)
        writer.write_str_value("region", self.region)
        writer.write_str_value("user_id", self.user_id)
    

