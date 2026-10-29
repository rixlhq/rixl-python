from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WebhookAttempt(Parsable):
    """
    WebhookAttempt is one recorded delivery attempt for an event/endpoint pair.
    """
    # The attempt property
    attempt: Optional[int] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The duration_ms property
    duration_ms: Optional[int] = None
    # The error property
    error: Optional[str] = None
    # The event_id property
    event_id: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # True when this delivery was triggered by ReplayEvent or SendTestEvent rather than the original subscription fan-out.
    replay: Optional[bool] = None
    # First 1 KiB of the endpoint's response body.
    response_snippet: Optional[str] = None
    # The status_code property
    status_code: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebhookAttempt:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebhookAttempt
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebhookAttempt()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "attempt": lambda n : setattr(self, 'attempt', n.get_int_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "duration_ms": lambda n : setattr(self, 'duration_ms', n.get_int_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "event_id": lambda n : setattr(self, 'event_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "replay": lambda n : setattr(self, 'replay', n.get_bool_value()),
            "response_snippet": lambda n : setattr(self, 'response_snippet', n.get_str_value()),
            "status_code": lambda n : setattr(self, 'status_code', n.get_int_value()),
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
        writer.write_int_value("attempt", self.attempt)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_int_value("duration_ms", self.duration_ms)
        writer.write_str_value("error", self.error)
        writer.write_str_value("event_id", self.event_id)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("replay", self.replay)
        writer.write_str_value("response_snippet", self.response_snippet)
        writer.write_int_value("status_code", self.status_code)
    

