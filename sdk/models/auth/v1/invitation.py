from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .invitation_inviter import InvitationInviter
    from .invitation_state import InvitationState
    from .membership_role import MembershipRole
    from .organization import Organization

@dataclass
class Invitation(Parsable):
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    created_at: Optional[datetime.datetime] = None
    # The email property
    email: Optional[str] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    expires_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # Unset once the inviter's account is deleted.
    invited_by: Optional[InvitationInviter] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    last_sent_at: Optional[datetime.datetime] = None
    # The org property
    org: Optional[Organization] = None
    # Set while a daily sending limit would delay a resend by the caller.
    resend_available_at: Optional[datetime.datetime] = None
    # Never OWNER.
    role: Optional[MembershipRole] = None
    # The effective state: a pending invitation past its expiry reads as expired.
    state: Optional[InvitationState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Invitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Invitation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Invitation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .invitation_inviter import InvitationInviter
        from .invitation_state import InvitationState
        from .membership_role import MembershipRole
        from .organization import Organization

        from .invitation_inviter import InvitationInviter
        from .invitation_state import InvitationState
        from .membership_role import MembershipRole
        from .organization import Organization

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "invited_by": lambda n : setattr(self, 'invited_by', n.get_object_value(InvitationInviter)),
            "last_sent_at": lambda n : setattr(self, 'last_sent_at', n.get_datetime_value()),
            "org": lambda n : setattr(self, 'org', n.get_object_value(Organization)),
            "resend_available_at": lambda n : setattr(self, 'resend_available_at', n.get_datetime_value()),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_str_value("id", self.id)
        writer.write_object_value("invited_by", self.invited_by)
        writer.write_datetime_value("last_sent_at", self.last_sent_at)
        writer.write_object_value("org", self.org)
        writer.write_datetime_value("resend_available_at", self.resend_available_at)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("state", self.state)
    

