from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FeedsPostRequestBody(Parsable):
    # The allowImages property
    allow_images: Optional[bool] = None
    # The allowVideos property
    allow_videos: Optional[bool] = None
    # The description property
    description: Optional[str] = None
    # The hasComments property
    has_comments: Optional[bool] = None
    # The hasLikes property
    has_likes: Optional[bool] = None
    # The hasShares property
    has_shares: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeedsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeedsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeedsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowImages": lambda n : setattr(self, 'allow_images', n.get_bool_value()),
            "allowVideos": lambda n : setattr(self, 'allow_videos', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "hasComments": lambda n : setattr(self, 'has_comments', n.get_bool_value()),
            "hasLikes": lambda n : setattr(self, 'has_likes', n.get_bool_value()),
            "hasShares": lambda n : setattr(self, 'has_shares', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_bool_value("allowImages", self.allow_images)
        writer.write_bool_value("allowVideos", self.allow_videos)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("hasComments", self.has_comments)
        writer.write_bool_value("hasLikes", self.has_likes)
        writer.write_bool_value("hasShares", self.has_shares)
        writer.write_str_value("name", self.name)
    

