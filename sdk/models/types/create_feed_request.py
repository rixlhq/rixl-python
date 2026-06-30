from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CreateFeedRequest(AdditionalDataHolder, Parsable):
    """
    Feed details
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The allow_images property
    allow_images: Optional[bool] = None
    # The allow_videos property
    allow_videos: Optional[bool] = None
    # The description property
    description: Optional[str] = None
    # The has_comments property
    has_comments: Optional[bool] = None
    # The has_likes property
    has_likes: Optional[bool] = None
    # The has_shares property
    has_shares: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateFeedRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateFeedRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateFeedRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allow_images": lambda n : setattr(self, 'allow_images', n.get_bool_value()),
            "allow_videos": lambda n : setattr(self, 'allow_videos', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "has_comments": lambda n : setattr(self, 'has_comments', n.get_bool_value()),
            "has_likes": lambda n : setattr(self, 'has_likes', n.get_bool_value()),
            "has_shares": lambda n : setattr(self, 'has_shares', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
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
        writer.write_bool_value("allow_images", self.allow_images)
        writer.write_bool_value("allow_videos", self.allow_videos)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("has_comments", self.has_comments)
        writer.write_bool_value("has_likes", self.has_likes)
        writer.write_bool_value("has_shares", self.has_shares)
        writer.write_str_value("name", self.name)
        writer.write_str_value("project_id", self.project_id)
        writer.write_additional_data_value(self.additional_data)
    

