from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...common.v1.file import File
    from ...common.v1.visibility import Visibility

@dataclass
class Image(Parsable):
    # The attached_to_video property
    attached_to_video: Optional[bool] = None
    # The file property
    file: Optional[File] = None
    # The height property
    height: Optional[int] = None
    # The id property
    id: Optional[str] = None
    # The thumbhash property
    thumbhash: Optional[str] = None
    # The visibility property
    visibility: Optional[Visibility] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Image:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Image
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Image()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...common.v1.file import File
        from ...common.v1.visibility import Visibility

        from ...common.v1.file import File
        from ...common.v1.visibility import Visibility

        fields: dict[str, Callable[[Any], None]] = {
            "attached_to_video": lambda n : setattr(self, 'attached_to_video', n.get_bool_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(File)),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "thumbhash": lambda n : setattr(self, 'thumbhash', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(Visibility)),
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
        writer.write_bool_value("attached_to_video", self.attached_to_video)
        writer.write_object_value("file", self.file)
        writer.write_int_value("height", self.height)
        writer.write_str_value("id", self.id)
        writer.write_str_value("thumbhash", self.thumbhash)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_int_value("width", self.width)
    

