from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.auth.v1.membership_application_state import MembershipApplicationState
    from .with_user_patch_request_body_user import WithUser_PatchRequestBody_user

@dataclass
class WithUser_PatchRequestBody(Parsable):
    # The state property
    state: Optional[MembershipApplicationState] = None
    # The user property
    user: Optional[WithUser_PatchRequestBody_user] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithUser_PatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithUser_PatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithUser_PatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.auth.v1.membership_application_state import MembershipApplicationState
        from .with_user_patch_request_body_user import WithUser_PatchRequestBody_user

        from .......models.auth.v1.membership_application_state import MembershipApplicationState
        from .with_user_patch_request_body_user import WithUser_PatchRequestBody_user

        fields: dict[str, Callable[[Any], None]] = {
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MembershipApplicationState)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(WithUser_PatchRequestBody_user)),
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
        writer.write_enum_value("state", self.state)
        writer.write_object_value("user", self.user)
    

