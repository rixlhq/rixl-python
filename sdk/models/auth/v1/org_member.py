from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .membership_role import MembershipRole
    from .membership_state import MembershipState

@dataclass
class OrgMember(Parsable):
    # The first_name property
    first_name: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The invitation_expires_at property
    invitation_expires_at: Optional[datetime.datetime] = None
    # The joined_at property
    joined_at: Optional[datetime.datetime] = None
    # The last_name property
    last_name: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The role property
    role: Optional[MembershipRole] = None
    # The state property
    state: Optional[MembershipState] = None
    # The user_id property
    user_id: Optional[str] = None
    # The username property
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrgMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrgMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrgMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .membership_role import MembershipRole
        from .membership_state import MembershipState

        from .membership_role import MembershipRole
        from .membership_state import MembershipState

        fields: dict[str, Callable[[Any], None]] = {
            "first_name": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "invitation_expires_at": lambda n : setattr(self, 'invitation_expires_at', n.get_datetime_value()),
            "joined_at": lambda n : setattr(self, 'joined_at', n.get_datetime_value()),
            "last_name": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MembershipRole)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MembershipState)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
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
        writer.write_str_value("first_name", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("invitation_expires_at", self.invitation_expires_at)
        writer.write_datetime_value("joined_at", self.joined_at)
        writer.write_str_value("last_name", self.last_name)
        writer.write_str_value("org_id", self.org_id)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("user_id", self.user_id)
        writer.write_str_value("username", self.username)
    

