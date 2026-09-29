from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.common.v1.visibility import Visibility

@dataclass
class VisibilityPatchRequestBody(Parsable):
    # The image_id property
    image_id: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    # The visibility property
    visibility: Optional[Visibility] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VisibilityPatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VisibilityPatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VisibilityPatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.common.v1.visibility import Visibility

        from ........models.common.v1.visibility import Visibility

        fields: dict[str, Callable[[Any], None]] = {
            "image_id": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(Visibility)),
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
        writer.write_str_value("image_id", self.image_id)
        writer.write_str_value("project_id", self.project_id)
        writer.write_enum_value("visibility", self.visibility)
    

