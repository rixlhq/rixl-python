from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_priority import TicketPriority
    from .ticket_status import TicketStatus

@dataclass
class Ticket(Parsable):
    # The category_id property
    category_id: Optional[str] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The priority property
    priority: Optional[TicketPriority] = None
    # The project_id property
    project_id: Optional[str] = None
    # The status property
    status: Optional[TicketStatus] = None
    # The subject property
    subject: Optional[str] = None
    # The topic_id property
    topic_id: Optional[str] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    # The user_id property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Ticket:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Ticket
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Ticket()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_priority import TicketPriority
        from .ticket_status import TicketStatus

        from .ticket_priority import TicketPriority
        from .ticket_status import TicketStatus

        fields: dict[str, Callable[[Any], None]] = {
            "category_id": lambda n : setattr(self, 'category_id', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(TicketPriority)),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TicketStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "topic_id": lambda n : setattr(self, 'topic_id', n.get_str_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
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
        writer.write_str_value("category_id", self.category_id)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("org_id", self.org_id)
        writer.write_enum_value("priority", self.priority)
        writer.write_str_value("project_id", self.project_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("topic_id", self.topic_id)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_str_value("user_id", self.user_id)
    

