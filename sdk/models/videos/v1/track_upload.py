from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .track_upload_target import TrackUploadTarget

@dataclass
class TrackUpload(Parsable):
    # The expires_at property
    expires_at: Optional[datetime.datetime] = None
    # The targets property
    targets: Optional[list[TrackUploadTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrackUpload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrackUpload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrackUpload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .track_upload_target import TrackUploadTarget

        from .track_upload_target import TrackUploadTarget

        fields: dict[str, Callable[[Any], None]] = {
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(TrackUploadTarget)),
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
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_collection_of_object_values("targets", self.targets)
    

