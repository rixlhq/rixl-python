from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExportDashboardResponse(Parsable):
    # The content property
    content: Optional[bytes] = None
    # The content_type property
    content_type: Optional[str] = None
    # The filename property
    filename: Optional[str] = None
    # The row_count property
    row_count: Optional[int] = None
    # The widget_count property
    widget_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExportDashboardResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportDashboardResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExportDashboardResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "filename": lambda n : setattr(self, 'filename', n.get_str_value()),
            "row_count": lambda n : setattr(self, 'row_count', n.get_int_value()),
            "widget_count": lambda n : setattr(self, 'widget_count', n.get_int_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_str_value("content_type", self.content_type)
        writer.write_str_value("filename", self.filename)
        writer.write_int_value("row_count", self.row_count)
        writer.write_int_value("widget_count", self.widget_count)
    

