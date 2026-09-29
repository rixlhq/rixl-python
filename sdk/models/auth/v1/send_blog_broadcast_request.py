from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SendBlogBroadcastRequest(Parsable):
    # The category property
    category: Optional[str] = None
    # The commit_sha property
    commit_sha: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The published_at property
    published_at: Optional[datetime.datetime] = None
    # The slug property
    slug: Optional[str] = None
    # The title property
    title: Optional[str] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SendBlogBroadcastRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendBlogBroadcastRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SendBlogBroadcastRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "commit_sha": lambda n : setattr(self, 'commit_sha', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "published_at": lambda n : setattr(self, 'published_at', n.get_datetime_value()),
            "slug": lambda n : setattr(self, 'slug', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_datetime_value("published_at", self.published_at)
        writer.write_str_value("slug", self.slug)
        writer.write_str_value("title", self.title)
        writer.write_str_value("url", self.url)
    

