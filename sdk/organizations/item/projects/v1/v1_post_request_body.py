from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.common.v1.video_quality import VideoQuality

@dataclass
class V1PostRequestBody(Parsable):
    # The name property
    name: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The regions property
    regions: Optional[list[str]] = None
    # The video_quality property
    video_quality: Optional[VideoQuality] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> V1PostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: V1PostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return V1PostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.common.v1.video_quality import VideoQuality

        from .....models.common.v1.video_quality import VideoQuality

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "regions": lambda n : setattr(self, 'regions', n.get_collection_of_primitive_values(str)),
            "video_quality": lambda n : setattr(self, 'video_quality', n.get_enum_value(VideoQuality)),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("org_id", self.org_id)
        writer.write_collection_of_primitive_values("regions", self.regions)
        writer.write_enum_value("video_quality", self.video_quality)
    

