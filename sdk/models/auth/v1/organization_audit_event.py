from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...google.protobuf.struct import Struct

@dataclass
class OrganizationAuditEvent(Parsable):
    # The action property
    action: Optional[str] = None
    # The actor_id property
    actor_id: Optional[str] = None
    # The actor_type property
    actor_type: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # A JSON object whose property values may be any JSON value.
    metadata: Optional[Struct] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    occurred_at: Optional[datetime.datetime] = None
    # The org_id property
    org_id: Optional[str] = None
    # The target_id property
    target_id: Optional[str] = None
    # The target_type property
    target_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationAuditEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationAuditEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationAuditEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...google.protobuf.struct import Struct

        from ...google.protobuf.struct import Struct

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "actor_id": lambda n : setattr(self, 'actor_id', n.get_str_value()),
            "actor_type": lambda n : setattr(self, 'actor_type', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(Struct)),
            "occurred_at": lambda n : setattr(self, 'occurred_at', n.get_datetime_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "target_id": lambda n : setattr(self, 'target_id', n.get_str_value()),
            "target_type": lambda n : setattr(self, 'target_type', n.get_str_value()),
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
        writer.write_str_value("action", self.action)
        writer.write_str_value("actor_id", self.actor_id)
        writer.write_str_value("actor_type", self.actor_type)
        writer.write_str_value("id", self.id)
        writer.write_object_value("metadata", self.metadata)
        writer.write_datetime_value("occurred_at", self.occurred_at)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("target_id", self.target_id)
        writer.write_str_value("target_type", self.target_type)
    

