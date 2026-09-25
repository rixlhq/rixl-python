from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.analytics.v1.export_format import ExportFormat

@dataclass
class ExportPostRequestBody(Parsable):
    # The dashboard_id property
    dashboard_id: Optional[str] = None
    # The format property
    format: Optional[ExportFormat] = None
    # The time_end property
    time_end: Optional[str] = None
    # The time_start property
    time_start: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExportPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.analytics.v1.export_format import ExportFormat

        from ......models.analytics.v1.export_format import ExportFormat

        fields: dict[str, Callable[[Any], None]] = {
            "dashboard_id": lambda n : setattr(self, 'dashboard_id', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_enum_value(ExportFormat)),
            "time_end": lambda n : setattr(self, 'time_end', n.get_str_value()),
            "time_start": lambda n : setattr(self, 'time_start', n.get_str_value()),
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
        writer.write_enum_value("format", self.format)
        writer.write_str_value("time_end", self.time_end)
        writer.write_str_value("time_start", self.time_start)
    

