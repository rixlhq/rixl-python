from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image_summary import ImageSummary

@dataclass
class ListImagesResponse(Parsable):
    # The images property
    images: Optional[list[ImageSummary]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListImagesResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListImagesResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListImagesResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .image_summary import ImageSummary

        from .image_summary import ImageSummary

        fields: dict[str, Callable[[Any], None]] = {
            "images": lambda n : setattr(self, 'images', n.get_collection_of_object_values(ImageSummary)),
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
        writer.write_collection_of_object_values("images", self.images)
    

