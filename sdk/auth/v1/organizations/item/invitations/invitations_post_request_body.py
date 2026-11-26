from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.auth.v1.membership_role import MembershipRole

@dataclass
class InvitationsPostRequestBody(Parsable):
    # Trimmed and lowercased before validation as a bare email address. The normalized address must be nonempty and at most 254 UTF-8 bytes, with a local part of at most 64 bytes and a domain containing a dot that is neither leading nor trailing.
    email: Optional[str] = None
    # Optional UUID that makes retries of the same create safe.
    request_id: Optional[str] = None
    # The role property
    role: Optional[MembershipRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvitationsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvitationsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvitationsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.auth.v1.membership_role import MembershipRole

        from ......models.auth.v1.membership_role import MembershipRole

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "request_id": lambda n : setattr(self, 'request_id', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("request_id", self.request_id)
        writer.write_enum_value("role", self.role)
    

