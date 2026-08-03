from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image import Image

@dataclass
class GetImageResponse(Parsable):
    # The image property
    image: Optional[Image] = None
    
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
        from .image import Image

        from .image import Image

        fields: dict[str, Callable[[Any], None]] = {
            "image": lambda n : setattr(self, 'image', n.get_object_value(Image)),
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
        writer.write_object_value("image", self.image)
    

