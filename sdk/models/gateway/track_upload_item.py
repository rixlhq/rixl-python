from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TrackUploadItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The file_name property
    file_name: Optional[str] = None
    # The format property
    format: Optional[str] = None
    # The label property
    label: Optional[str] = None
    # The language_code property
    language_code: Optional[str] = None
    # The size property
    size: Optional[int] = None
    
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
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "language_code": lambda n : setattr(self, 'language_code', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_str_value("file_name", self.file_name)
        writer.write_str_value("format", self.format)
        writer.write_str_value("label", self.label)
        writer.write_str_value("language_code", self.language_code)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    

