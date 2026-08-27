from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.google.protobuf.timestamp import Timestamp
    from .with_key_patch_request_body_expiring_at_member1 import WithKey_PatchRequestBody_expiring_atMember1

@dataclass
class WithKey_PatchRequestBody_expiring_at(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes Timestamp, WithKey_PatchRequestBody_expiring_atMember1
    """
    # Composed type representation for type Timestamp
    timestamp: Optional[Timestamp] = None
    # Composed type representation for type WithKey_PatchRequestBody_expiring_atMember1
    with_key_patch_request_body_expiring_at_member1: Optional[WithKey_PatchRequestBody_expiring_atMember1] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithKey_PatchRequestBody_expiring_at:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithKey_PatchRequestBody_expiring_at
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = WithKey_PatchRequestBody_expiring_at()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.google.protobuf.timestamp import Timestamp
        from .with_key_patch_request_body_expiring_at_member1 import WithKey_PatchRequestBody_expiring_atMember1

        if self.timestamp:
            return self.timestamp.get_field_deserializers()
        if self.with_key_patch_request_body_expiring_at_member1:
            return self.with_key_patch_request_body_expiring_at_member1.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.timestamp:
            writer.write_object_value(None, self.timestamp)
        elif self.with_key_patch_request_body_expiring_at_member1:
            writer.write_object_value(None, self.with_key_patch_request_body_expiring_at_member1)
    

