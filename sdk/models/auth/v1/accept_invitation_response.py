from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .membership_role import MembershipRole
    from .organization import Organization

@dataclass
class AcceptInvitationResponse(Parsable):
    # The org_id property
    org_id: Optional[str] = None
    # The organization property
    organization: Optional[Organization] = None
    # The role property
    role: Optional[MembershipRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AcceptInvitationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AcceptInvitationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AcceptInvitationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .membership_role import MembershipRole
        from .organization import Organization

        from .membership_role import MembershipRole
        from .organization import Organization

        fields: dict[str, Callable[[Any], None]] = {
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(Organization)),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MembershipRole)),
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
        writer.write_str_value("org_id", self.org_id)
        writer.write_object_value("organization", self.organization)
        writer.write_enum_value("role", self.role)
    

