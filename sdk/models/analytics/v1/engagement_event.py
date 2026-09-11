from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class EngagementEvent(Parsable):
    # The comment_text property
    comment_text: Optional[str] = None
    # The country property
    country: Optional[str] = None
    # The device_type property
    device_type: Optional[str] = None
    # The engagement_type property
    engagement_type: Optional[str] = None
    # The page property
    page: Optional[str] = None
    # The resource_id property
    resource_id: Optional[str] = None
    # The resource_type property
    resource_type: Optional[str] = None
    # The share_platform property
    share_platform: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EngagementEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EngagementEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EngagementEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "comment_text": lambda n : setattr(self, 'comment_text', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "engagement_type": lambda n : setattr(self, 'engagement_type', n.get_str_value()),
            "page": lambda n : setattr(self, 'page', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "resource_type": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "share_platform": lambda n : setattr(self, 'share_platform', n.get_str_value()),
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
        writer.write_str_value("comment_text", self.comment_text)
        writer.write_str_value("country", self.country)
        writer.write_str_value("device_type", self.device_type)
        writer.write_str_value("engagement_type", self.engagement_type)
        writer.write_str_value("page", self.page)
        writer.write_str_value("resource_id", self.resource_id)
        writer.write_str_value("resource_type", self.resource_type)
        writer.write_str_value("share_platform", self.share_platform)
    

