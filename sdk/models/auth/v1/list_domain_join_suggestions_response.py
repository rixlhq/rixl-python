from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization import Organization

@dataclass
class ListDomainJoinSuggestionsResponse(Parsable):
    # The next_page_token property
    next_page_token: Optional[str] = None
    # The organizations property
    organizations: Optional[list[Organization]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListDomainJoinSuggestionsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListDomainJoinSuggestionsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListDomainJoinSuggestionsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization import Organization

        from .organization import Organization

        fields: dict[str, Callable[[Any], None]] = {
            "next_page_token": lambda n : setattr(self, 'next_page_token', n.get_str_value()),
            "organizations": lambda n : setattr(self, 'organizations', n.get_collection_of_object_values(Organization)),
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
        writer.write_str_value("next_page_token", self.next_page_token)
        writer.write_collection_of_object_values("organizations", self.organizations)
    

