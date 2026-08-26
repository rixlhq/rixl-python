from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket import Ticket

@dataclass
class ListTicketsResponse(Parsable):
    # Maximum number of items returned.
    limit: Optional[int] = None
    # Number of items skipped before this page.
    offset: Optional[int] = None
    # The tickets property
    tickets: Optional[list[Ticket]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListTicketsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListTicketsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListTicketsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket import Ticket

        from .ticket import Ticket

        fields: dict[str, Callable[[Any], None]] = {
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
            "tickets": lambda n : setattr(self, 'tickets', n.get_collection_of_object_values(Ticket)),
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
        writer.write_int_value("limit", self.limit)
        writer.write_int_value("offset", self.offset)
        writer.write_collection_of_object_values("tickets", self.tickets)
    

