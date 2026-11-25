from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .invitation_state import InvitationState
    from .membership_role import MembershipRole

@dataclass
class LookupInvitationResponse(Parsable):
    """
    A closed invitation reports only its state.
    """
    # The email property
    email: Optional[str] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    expires_at: Optional[datetime.datetime] = None
    # The inviter_display_name property
    inviter_display_name: Optional[str] = None
    # The org_image_id property
    org_image_id: Optional[str] = None
    # The org_name property
    org_name: Optional[str] = None
    # The role property
    role: Optional[MembershipRole] = None
    # The state property
    state: Optional[InvitationState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LookupInvitationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LookupInvitationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LookupInvitationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .invitation_state import InvitationState
        from .membership_role import MembershipRole

        from .invitation_state import InvitationState
        from .membership_role import MembershipRole

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "inviter_display_name": lambda n : setattr(self, 'inviter_display_name', n.get_str_value()),
            "org_image_id": lambda n : setattr(self, 'org_image_id', n.get_str_value()),
            "org_name": lambda n : setattr(self, 'org_name', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MembershipRole)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(InvitationState)),
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
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_str_value("inviter_display_name", self.inviter_display_name)
        writer.write_str_value("org_image_id", self.org_image_id)
        writer.write_str_value("org_name", self.org_name)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("state", self.state)
    

