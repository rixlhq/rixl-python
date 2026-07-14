from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.auth.v1.membership_state import MembershipState
    from ......models.auth.v1.user_org_request import UserOrgRequest

@dataclass
class StatePatchRequestBody(Parsable):
    # The state property
    state: Optional[MembershipState] = None
    # The user property
    user: Optional[UserOrgRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatePatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatePatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatePatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.auth.v1.membership_state import MembershipState
        from ......models.auth.v1.user_org_request import UserOrgRequest

        from ......models.auth.v1.membership_state import MembershipState
        from ......models.auth.v1.user_org_request import UserOrgRequest

        fields: dict[str, Callable[[Any], None]] = {
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MembershipState)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(UserOrgRequest)),
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
    

