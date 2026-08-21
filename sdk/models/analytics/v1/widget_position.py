from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WidgetPosition(Parsable):
    """
    WidgetPosition is expressed in grid units, never pixels.
    """
    # The height property
    height: Optional[int] = None
    # The pos_x property
    pos_x: Optional[int] = None
    # The pos_y property
    pos_y: Optional[int] = None
    # The sort_order property
    sort_order: Optional[int] = None
    # The widget_id property
    widget_id: Optional[str] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WidgetPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WidgetPosition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WidgetPosition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "pos_x": lambda n : setattr(self, 'pos_x', n.get_int_value()),
            "pos_y": lambda n : setattr(self, 'pos_y', n.get_int_value()),
            "sort_order": lambda n : setattr(self, 'sort_order', n.get_int_value()),
            "widget_id": lambda n : setattr(self, 'widget_id', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_int_value("height", self.height)
        writer.write_int_value("pos_x", self.pos_x)
        writer.write_int_value("pos_y", self.pos_y)
        writer.write_int_value("sort_order", self.sort_order)
        writer.write_str_value("widget_id", self.widget_id)
        writer.write_int_value("width", self.width)
    

