from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PolicyAttachment(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The identity_id property
    identity_id: Optional[str] = None
    # The identity_type property
    identity_type: Optional[str] = None
    # The policy_id property
    policy_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyAttachment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyAttachment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "identity_id": lambda n : setattr(self, 'identity_id', n.get_str_value()),
            "identity_type": lambda n : setattr(self, 'identity_type', n.get_str_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
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
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("identity_id", self.identity_id)
        writer.write_str_value("identity_type", self.identity_type)
        writer.write_str_value("policy_id", self.policy_id)
        writer.write_additional_data_value(self.additional_data)
    

