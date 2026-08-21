from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.analytics.v1.widget_position import WidgetPosition

@dataclass
class LayoutPostRequestBody(Parsable):
    # The dashboard_id property
    dashboard_id: Optional[str] = None
    # The expected_revision property
    expected_revision: Optional[int] = None
    # The positions property
    positions: Optional[list[WidgetPosition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LayoutPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LayoutPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LayoutPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.analytics.v1.widget_position import WidgetPosition

        from ......models.analytics.v1.widget_position import WidgetPosition

        fields: dict[str, Callable[[Any], None]] = {
            "dashboard_id": lambda n : setattr(self, 'dashboard_id', n.get_str_value()),
            "expected_revision": lambda n : setattr(self, 'expected_revision', n.get_int_value()),
            "positions": lambda n : setattr(self, 'positions', n.get_collection_of_object_values(WidgetPosition)),
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
        writer.write_str_value("dashboard_id", self.dashboard_id)
        writer.write_int_value("expected_revision", self.expected_revision)
        writer.write_collection_of_object_values("positions", self.positions)
    

