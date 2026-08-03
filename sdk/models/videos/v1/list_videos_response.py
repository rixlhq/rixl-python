from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .video import Video

@dataclass
class ListVideosResponse(Parsable):
    # Maximum number of items returned.
    limit: Optional[int] = None
    # Number of items skipped before this page.
    offset: Optional[int] = None
    # The sort_direction property
    sort_direction: Optional[str] = None
    # The sort_field property
    sort_field: Optional[str] = None
    # The videos property
    videos: Optional[list[Video]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListVideosResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListVideosResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListVideosResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .video import Video

        from .video import Video

        fields: dict[str, Callable[[Any], None]] = {
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
            "sort_direction": lambda n : setattr(self, 'sort_direction', n.get_str_value()),
            "sort_field": lambda n : setattr(self, 'sort_field', n.get_str_value()),
            "videos": lambda n : setattr(self, 'videos', n.get_collection_of_object_values(Video)),
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
        writer.write_int_value("limit", self.limit)
        writer.write_int_value("offset", self.offset)
        writer.write_str_value("sort_direction", self.sort_direction)
        writer.write_str_value("sort_field", self.sort_field)
        writer.write_collection_of_object_values("videos", self.videos)
    

