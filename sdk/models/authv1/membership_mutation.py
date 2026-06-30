from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MembershipMutation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The joined_at property
    joined_at: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The org_name property
    org_name: Optional[str] = None
    # The role property
    role: Optional[str] = None
    # The state property
    state: Optional[str] = None
    # The user_id property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MembershipMutation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MembershipMutation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MembershipMutation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "joined_at": lambda n : setattr(self, 'joined_at', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "org_name": lambda n : setattr(self, 'org_name', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_str_value("joined_at", self.joined_at)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("org_name", self.org_name)
        writer.write_str_value("role", self.role)
        writer.write_str_value("state", self.state)
        writer.write_str_value("user_id", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

