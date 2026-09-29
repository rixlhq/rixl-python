from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_priority import TicketPriority

@dataclass
class CreateTicketRequest(Parsable):
    # The category_id property
    category_id: Optional[str] = None
    # The message property
    message: Optional[str] = None
    # The priority property
    priority: Optional[TicketPriority] = None
    # The project_id property
    project_id: Optional[str] = None
    # The subject property
    subject: Optional[str] = None
    # The topic_id property
    topic_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateTicketRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateTicketRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateTicketRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_priority import TicketPriority

        from .ticket_priority import TicketPriority

        fields: dict[str, Callable[[Any], None]] = {
            "category_id": lambda n : setattr(self, 'category_id', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(TicketPriority)),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "topic_id": lambda n : setattr(self, 'topic_id', n.get_str_value()),
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
        writer.write_str_value("category_id", self.category_id)
        writer.write_str_value("message", self.message)
        writer.write_enum_value("priority", self.priority)
        writer.write_str_value("project_id", self.project_id)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("topic_id", self.topic_id)
    

