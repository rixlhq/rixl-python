from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.auth.v1.policy_identity_type import PolicyIdentityType
    from ........models.auth.v1.user_org_request import UserOrgRequest

@dataclass
class AttachmentsPostRequestBody(Parsable):
    # The identity_id property
    identity_id: Optional[str] = None
    # The identity_type property
    identity_type: Optional[PolicyIdentityType] = None
    # The policy_id property
    policy_id: Optional[str] = None
    # The user property
    user: Optional[UserOrgRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttachmentsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttachmentsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttachmentsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.auth.v1.policy_identity_type import PolicyIdentityType
        from ........models.auth.v1.user_org_request import UserOrgRequest

        from ........models.auth.v1.policy_identity_type import PolicyIdentityType
        from ........models.auth.v1.user_org_request import UserOrgRequest

        fields: dict[str, Callable[[Any], None]] = {
            "identity_id": lambda n : setattr(self, 'identity_id', n.get_str_value()),
            "identity_type": lambda n : setattr(self, 'identity_type', n.get_enum_value(PolicyIdentityType)),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
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
        writer.write_str_value("identity_id", self.identity_id)
        writer.write_enum_value("identity_type", self.identity_type)
        writer.write_str_value("policy_id", self.policy_id)
        writer.write_object_value("user", self.user)
    

