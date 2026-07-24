from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CompletePostRequestBody(Parsable):
    # The attached_to_video property
    attached_to_video: Optional[bool] = None
    # The image_id property
    image_id: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompletePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompletePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompletePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "attached_to_video": lambda n : setattr(self, 'attached_to_video', n.get_bool_value()),
            "image_id": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
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
        writer.write_bool_value("attached_to_video", self.attached_to_video)
        writer.write_str_value("image_id", self.image_id)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("project_id", self.project_id)
    

