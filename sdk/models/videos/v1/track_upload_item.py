from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TrackUploadItem(Parsable):
    # The fileName property
    file_name: Optional[str] = None
    # The format property
    format: Optional[str] = None
    # The label property
    label: Optional[str] = None
    # The languageCode property
    language_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrackUploadItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrackUploadItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrackUploadItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "languageCode": lambda n : setattr(self, 'language_code', n.get_str_value()),
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
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("format", self.format)
        writer.write_str_value("label", self.label)
        writer.write_str_value("languageCode", self.language_code)
    

