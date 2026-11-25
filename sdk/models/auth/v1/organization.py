from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Organization(Parsable):
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    created_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The image_id property
    image_id: Optional[str] = None
    # The internal property
    internal: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # The personal property
    personal: Optional[bool] = None
    # The slug property
    slug: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Organization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Organization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Organization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "image_id": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "personal": lambda n : setattr(self, 'personal', n.get_bool_value()),
            "slug": lambda n : setattr(self, 'slug', n.get_str_value()),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("image_id", self.image_id)
        writer.write_bool_value("internal", self.internal)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("personal", self.personal)
        writer.write_str_value("slug", self.slug)
    

