from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class VideoUploadInit(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The expires_at property
    expires_at: Optional[str] = None
    # The poster_id property
    poster_id: Optional[str] = None
    # The poster_upload_url property
    poster_upload_url: Optional[str] = None
    # The video_id property
    video_id: Optional[str] = None
    # The video_upload_url property
    video_upload_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VideoUploadInit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VideoUploadInit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VideoUploadInit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_str_value()),
            "poster_id": lambda n : setattr(self, 'poster_id', n.get_str_value()),
            "poster_upload_url": lambda n : setattr(self, 'poster_upload_url', n.get_str_value()),
            "video_id": lambda n : setattr(self, 'video_id', n.get_str_value()),
            "video_upload_url": lambda n : setattr(self, 'video_upload_url', n.get_str_value()),
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
        writer.write_str_value("expires_at", self.expires_at)
        writer.write_str_value("poster_id", self.poster_id)
        writer.write_str_value("poster_upload_url", self.poster_upload_url)
        writer.write_str_value("video_id", self.video_id)
        writer.write_str_value("video_upload_url", self.video_upload_url)
        writer.write_additional_data_value(self.additional_data)
    

