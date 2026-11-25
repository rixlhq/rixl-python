from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .kind import Kind

@dataclass
class UserDeletionPlanEntry(Parsable):
    # Set when another member will lose access to the personal org.
    affected_user_id: Optional[str] = None
    # The affected_username property
    affected_username: Optional[str] = None
    # The kind property
    kind: Optional[Kind] = None
    # The org_id property
    org_id: Optional[str] = None
    # The org_name property
    org_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserDeletionPlanEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserDeletionPlanEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserDeletionPlanEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .kind import Kind

        from .kind import Kind

        fields: dict[str, Callable[[Any], None]] = {
            "affected_user_id": lambda n : setattr(self, 'affected_user_id', n.get_str_value()),
            "affected_username": lambda n : setattr(self, 'affected_username', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(Kind)),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "org_name": lambda n : setattr(self, 'org_name', n.get_str_value()),
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
        writer.write_str_value("affected_user_id", self.affected_user_id)
        writer.write_str_value("affected_username", self.affected_username)
        writer.write_enum_value("kind", self.kind)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("org_name", self.org_name)
    

