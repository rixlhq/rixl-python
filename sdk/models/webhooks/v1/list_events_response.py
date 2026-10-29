from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .webhook_event import WebhookEvent

@dataclass
class ListEventsResponse(Parsable):
    # The events property
    events: Optional[list[WebhookEvent]] = None
    # The limit property
    limit: Optional[int] = None
    # The offset property
    offset: Optional[int] = None
    # The total property
    total: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListEventsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListEventsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListEventsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .webhook_event import WebhookEvent

        from .webhook_event import WebhookEvent

        fields: dict[str, Callable[[Any], None]] = {
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(WebhookEvent)),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
            "total": lambda n : setattr(self, 'total', n.get_str_value()),
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
        writer.write_collection_of_object_values("events", self.events)
        writer.write_int_value("limit", self.limit)
        writer.write_int_value("offset", self.offset)
        writer.write_str_value("total", self.total)
    

