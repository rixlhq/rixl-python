from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.videos.v1.track_upload_item import TrackUploadItem

@dataclass
class UploadPostRequestBody(Parsable):
    # The items property
    items: Optional[list[TrackUploadItem]] = None
    # The orgId property
    org_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UploadPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UploadPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UploadPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .........models.videos.v1.track_upload_item import TrackUploadItem

        from .........models.videos.v1.track_upload_item import TrackUploadItem

        fields: dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(TrackUploadItem)),
            "orgId": lambda n : setattr(self, 'org_id', n.get_str_value()),
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
        writer.write_str_value("orgId", self.org_id)
    

