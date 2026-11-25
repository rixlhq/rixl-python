from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .invitation import Invitation

@dataclass
class ListOrganizationInvitationsResponse(Parsable):
    # The invitations property
    invitations: Optional[list[Invitation]] = None
    # The next_page_token property
    next_page_token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListOrganizationInvitationsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListOrganizationInvitationsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListOrganizationInvitationsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .invitation import Invitation

        from .invitation import Invitation

        fields: dict[str, Callable[[Any], None]] = {
            "invitations": lambda n : setattr(self, 'invitations', n.get_collection_of_object_values(Invitation)),
            "next_page_token": lambda n : setattr(self, 'next_page_token', n.get_str_value()),
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
        writer.write_collection_of_object_values("invitations", self.invitations)
        writer.write_str_value("next_page_token", self.next_page_token)
    

