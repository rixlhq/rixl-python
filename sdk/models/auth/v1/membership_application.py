from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .membership_application_state import MembershipApplicationState
    from .membership_role import MembershipRole

@dataclass
class MembershipApplication(Parsable):
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The decided_at property
    decided_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The invitation_expires_at property
    invitation_expires_at: Optional[datetime.datetime] = None
    # The org_id property
    org_id: Optional[str] = None
    # The organization_first_name property
    organization_first_name: Optional[str] = None
    # The organization_last_name property
    organization_last_name: Optional[str] = None
    # The organization_username property
    organization_username: Optional[str] = None
    # The role property
    role: Optional[MembershipRole] = None
    # The state property
    state: Optional[MembershipApplicationState] = None
    # The user_id property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MembershipApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MembershipApplication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MembershipApplication()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .membership_application_state import MembershipApplicationState
        from .membership_role import MembershipRole

        from .membership_application_state import MembershipApplicationState
        from .membership_role import MembershipRole

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "decided_at": lambda n : setattr(self, 'decided_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "invitation_expires_at": lambda n : setattr(self, 'invitation_expires_at', n.get_datetime_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "organization_first_name": lambda n : setattr(self, 'organization_first_name', n.get_str_value()),
            "organization_last_name": lambda n : setattr(self, 'organization_last_name', n.get_str_value()),
            "organization_username": lambda n : setattr(self, 'organization_username', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MembershipRole)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MembershipApplicationState)),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_datetime_value("decided_at", self.decided_at)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("invitation_expires_at", self.invitation_expires_at)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("organization_first_name", self.organization_first_name)
        writer.write_str_value("organization_last_name", self.organization_last_name)
        writer.write_str_value("organization_username", self.organization_username)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("user_id", self.user_id)
    

