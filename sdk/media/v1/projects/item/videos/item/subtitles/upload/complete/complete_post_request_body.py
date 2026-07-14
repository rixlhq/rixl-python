from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..........models.videos.v1.complete_track_upload_item import CompleteTrackUploadItem

@dataclass
class CompletePostRequestBody(Parsable):
    # The items property
    items: Optional[list[CompleteTrackUploadItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompletePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompletePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompletePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..........models.videos.v1.complete_track_upload_item import CompleteTrackUploadItem

        from ..........models.videos.v1.complete_track_upload_item import CompleteTrackUploadItem

        fields: dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(CompleteTrackUploadItem)),
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
        writer.write_collection_of_object_values("items", self.items)
    

