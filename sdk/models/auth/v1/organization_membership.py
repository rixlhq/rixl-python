from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .membership_role import MembershipRole
    from .membership_state import MembershipState
    from .organization import Organization

@dataclass
class OrganizationMembership(Parsable):
    # The organization property
    organization: Optional[Organization] = None
    # The role property
    role: Optional[MembershipRole] = None
    # The state property
    state: Optional[MembershipState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationMembership:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationMembership
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationMembership()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .membership_role import MembershipRole
        from .membership_state import MembershipState
        from .organization import Organization

        from .membership_role import MembershipRole
        from .membership_state import MembershipState
        from .organization import Organization

        fields: dict[str, Callable[[Any], None]] = {
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(Organization)),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MembershipRole)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MembershipState)),
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
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("state", self.state)
    

