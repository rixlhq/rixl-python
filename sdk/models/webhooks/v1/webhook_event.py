from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...google.protobuf.struct import Struct

@dataclass
class WebhookEvent(Parsable):
    """
    WebhookEvent is a recorded outbound notification. `data` is the exact object embedded in the delivered payload envelope.
    """
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The data property
    data: Optional[Struct] = None
    # The id property
    id: Optional[str] = None
    # The resource_id property
    resource_id: Optional[str] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebhookEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebhookEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebhookEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...google.protobuf.struct import Struct

        from ...google.protobuf.struct import Struct

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "data": lambda n : setattr(self, 'data', n.get_object_value(Struct)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_object_value("data", self.data)
        writer.write_str_value("id", self.id)
        writer.write_str_value("resource_id", self.resource_id)
        writer.write_str_value("type", self.type)
    

