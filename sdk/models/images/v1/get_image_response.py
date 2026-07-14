from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...common.v1.visibility import Visibility
    from .image_file import ImageFile

@dataclass
class GetImageResponse(Parsable):
    # The attachedToVideo property
    attached_to_video: Optional[bool] = None
    # The file property
    file: Optional[ImageFile] = None
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
    def create_from_discriminator_value(parse_node: ParseNode) -> GetImageResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetImageResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetImageResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...common.v1.visibility import Visibility
        from .image_file import ImageFile

        from ...common.v1.visibility import Visibility
        from .image_file import ImageFile

        fields: dict[str, Callable[[Any], None]] = {
            "attachedToVideo": lambda n : setattr(self, 'attached_to_video', n.get_bool_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(ImageFile)),
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
        writer.write_bool_value("attachedToVideo", self.attached_to_video)
        writer.write_object_value("file", self.file)
        writer.write_int_value("height", self.height)
        writer.write_str_value("id", self.id)
        writer.write_str_value("thumbhash", self.thumbhash)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_int_value("width", self.width)
    

