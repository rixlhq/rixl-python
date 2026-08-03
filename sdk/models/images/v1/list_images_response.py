from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image import Image

@dataclass
class ListImagesResponse(Parsable):
    # The images property
    images: Optional[list[Image]] = None
    # Maximum number of items returned.
    limit: Optional[int] = None
    # Number of items skipped before this page.
    offset: Optional[int] = None
    # The sort_direction property
    sort_direction: Optional[str] = None
    # The sort_field property
    sort_field: Optional[str] = None
    
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
        from .image import Image

        from .image import Image

        fields: dict[str, Callable[[Any], None]] = {
            "images": lambda n : setattr(self, 'images', n.get_collection_of_object_values(Image)),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
            "sort_direction": lambda n : setattr(self, 'sort_direction', n.get_str_value()),
            "sort_field": lambda n : setattr(self, 'sort_field', n.get_str_value()),
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
        writer.write_int_value("limit", self.limit)
        writer.write_int_value("offset", self.offset)
        writer.write_str_value("sort_direction", self.sort_direction)
        writer.write_str_value("sort_field", self.sort_field)
    

