from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization import Organization

@dataclass
class ConvertToTeamOrganizationResponse(Parsable):
    # The organization property
    organization: Optional[Organization] = None
    # The personal_organization property
    personal_organization: Optional[Organization] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConvertToTeamOrganizationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConvertToTeamOrganizationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConvertToTeamOrganizationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization import Organization

        from .organization import Organization

        fields: dict[str, Callable[[Any], None]] = {
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(Organization)),
            "personal_organization": lambda n : setattr(self, 'personal_organization', n.get_object_value(Organization)),
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
        writer.write_object_value("organization", self.organization)
        writer.write_object_value("personal_organization", self.personal_organization)
    

