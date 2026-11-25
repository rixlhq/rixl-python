from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.auth.v1.organization import Organization

@dataclass
class WithOrg_PatchRequestBody(Parsable):
    # The organization property
    organization: Optional[Organization] = None
    # Supported paths are name, slug and image_id.
    update_mask: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithOrg_PatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithOrg_PatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithOrg_PatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.auth.v1.organization import Organization

        from .....models.auth.v1.organization import Organization

        fields: dict[str, Callable[[Any], None]] = {
            "organization": lambda n : setattr(self, 'organization', n.get_object_value(Organization)),
            "update_mask": lambda n : setattr(self, 'update_mask', n.get_str_value()),
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
        writer.write_object_value("organization", self.organization)
        writer.write_str_value("update_mask", self.update_mask)
    

