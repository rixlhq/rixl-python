from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GetVideoResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bitrate property
    bitrate: Optional[int] = None
    # The codec property
    codec: Optional[str] = None
    # The duration property
    duration: Optional[float] = None
    # The framerate property
    framerate: Optional[str] = None
    # The hdr property
    hdr: Optional[bool] = None
    # The height property
    height: Optional[int] = None
    # The id property
    id: Optional[str] = None
    # The visibility property
    visibility: Optional[int] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetVideoResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetVideoResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetVideoResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bitrate": lambda n : setattr(self, 'bitrate', n.get_int_value()),
            "codec": lambda n : setattr(self, 'codec', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_float_value()),
            "framerate": lambda n : setattr(self, 'framerate', n.get_str_value()),
            "hdr": lambda n : setattr(self, 'hdr', n.get_bool_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_int_value()),
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
        writer.write_int_value("bitrate", self.bitrate)
        writer.write_str_value("codec", self.codec)
        writer.write_float_value("duration", self.duration)
        writer.write_str_value("framerate", self.framerate)
        writer.write_bool_value("hdr", self.hdr)
        writer.write_int_value("height", self.height)
        writer.write_str_value("id", self.id)
        writer.write_int_value("visibility", self.visibility)
        writer.write_int_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    

