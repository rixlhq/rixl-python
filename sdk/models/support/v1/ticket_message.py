from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .message_author import MessageAuthor

@dataclass
class TicketMessage(Parsable):
    # The author_id property
    author_id: Optional[str] = None
    # The author_type property
    author_type: Optional[MessageAuthor] = None
    # The body property
    body: Optional[str] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The ticket_id property
    ticket_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .message_author import MessageAuthor

        from .message_author import MessageAuthor

        fields: dict[str, Callable[[Any], None]] = {
            "author_id": lambda n : setattr(self, 'author_id', n.get_str_value()),
            "author_type": lambda n : setattr(self, 'author_type', n.get_enum_value(MessageAuthor)),
            "body": lambda n : setattr(self, 'body', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "ticket_id": lambda n : setattr(self, 'ticket_id', n.get_str_value()),
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
        writer.write_str_value("author_id", self.author_id)
        writer.write_enum_value("author_type", self.author_type)
        writer.write_str_value("body", self.body)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("ticket_id", self.ticket_id)
    

