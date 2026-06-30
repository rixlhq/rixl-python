from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SendBlogBroadcastBody(AdditionalDataHolder, Parsable):
    """
    Broadcast payload
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The category property
    category: Optional[str] = None
    # The commit_sha property
    commit_sha: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The published_at property
    published_at: Optional[str] = None
    # The read_more_url property
    read_more_url: Optional[str] = None
    # The slug property
    slug: Optional[str] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SendBlogBroadcastBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendBlogBroadcastBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SendBlogBroadcastBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "commit_sha": lambda n : setattr(self, 'commit_sha', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "published_at": lambda n : setattr(self, 'published_at', n.get_str_value()),
            "read_more_url": lambda n : setattr(self, 'read_more_url', n.get_str_value()),
            "slug": lambda n : setattr(self, 'slug', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("category", self.category)
        writer.write_str_value("commit_sha", self.commit_sha)
        writer.write_str_value("description", self.description)
        writer.write_str_value("published_at", self.published_at)
        writer.write_str_value("read_more_url", self.read_more_url)
        writer.write_str_value("slug", self.slug)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

