from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket import Ticket
    from .ticket_message import TicketMessage

@dataclass
class GetTicketResponse(Parsable):
    # The messages property
    messages: Optional[list[TicketMessage]] = None
    # The ticket property
    ticket: Optional[Ticket] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetTicketResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetTicketResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetTicketResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket import Ticket
        from .ticket_message import TicketMessage

        from .ticket import Ticket
        from .ticket_message import TicketMessage

        fields: dict[str, Callable[[Any], None]] = {
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(TicketMessage)),
            "ticket": lambda n : setattr(self, 'ticket', n.get_object_value(Ticket)),
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
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_object_value("ticket", self.ticket)
    

