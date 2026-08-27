from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_key_patch_request_body_expiring_at import WithKey_PatchRequestBody_expiring_at

@dataclass
class WithKey_PatchRequestBody(Parsable):
    # The expiring_at property
    expiring_at: Optional[WithKey_PatchRequestBody_expiring_at] = None
    # The key_id property
    key_id: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The policy_ids property
    policy_ids: Optional[list[str]] = None
    # The replace_policies property
    replace_policies: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithKey_PatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithKey_PatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithKey_PatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .with_key_patch_request_body_expiring_at import WithKey_PatchRequestBody_expiring_at

        from .with_key_patch_request_body_expiring_at import WithKey_PatchRequestBody_expiring_at

        fields: dict[str, Callable[[Any], None]] = {
            "expiring_at": lambda n : setattr(self, 'expiring_at', n.get_object_value(WithKey_PatchRequestBody_expiring_at)),
            "key_id": lambda n : setattr(self, 'key_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "policy_ids": lambda n : setattr(self, 'policy_ids', n.get_collection_of_primitive_values(str)),
            "replace_policies": lambda n : setattr(self, 'replace_policies', n.get_bool_value()),
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
        writer.write_object_value("expiring_at", self.expiring_at)
        writer.write_str_value("key_id", self.key_id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("org_id", self.org_id)
        writer.write_collection_of_primitive_values("policy_ids", self.policy_ids)
        writer.write_bool_value("replace_policies", self.replace_policies)
    

