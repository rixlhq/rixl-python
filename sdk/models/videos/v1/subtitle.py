from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...common.v1.subtitle_format import SubtitleFormat

@dataclass
class Subtitle(Parsable):
    # The format property
    format: Optional[SubtitleFormat] = None
    # The id property
    id: Optional[str] = None
    # The label property
    label: Optional[str] = None
    # The language_code property
    language_code: Optional[str] = None
    # The video_id property
    video_id: Optional[str] = None
    # The vtt_path property
    vtt_path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Subtitle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Subtitle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Subtitle()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...common.v1.subtitle_format import SubtitleFormat

        from ...common.v1.subtitle_format import SubtitleFormat

        fields: dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_enum_value(SubtitleFormat)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "language_code": lambda n : setattr(self, 'language_code', n.get_str_value()),
            "video_id": lambda n : setattr(self, 'video_id', n.get_str_value()),
            "vtt_path": lambda n : setattr(self, 'vtt_path', n.get_str_value()),
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
        writer.write_enum_value("format", self.format)
        writer.write_str_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_str_value("language_code", self.language_code)
        writer.write_str_value("video_id", self.video_id)
        writer.write_str_value("vtt_path", self.vtt_path)
    

