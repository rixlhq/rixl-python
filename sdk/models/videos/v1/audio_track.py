from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AudioTrack(Parsable):
    # The codec property
    codec: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The label property
    label: Optional[str] = None
    # The languageCode property
    language_code: Optional[str] = None
    # The videoId property
    video_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AudioTrack:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AudioTrack
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AudioTrack()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "codec": lambda n : setattr(self, 'codec', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "languageCode": lambda n : setattr(self, 'language_code', n.get_str_value()),
            "videoId": lambda n : setattr(self, 'video_id', n.get_str_value()),
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
        writer.write_str_value("codec", self.codec)
        writer.write_str_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_str_value("languageCode", self.language_code)
        writer.write_str_value("videoId", self.video_id)
    

