from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dashboard_patch_request_body_visibility import Dashboard_PatchRequestBody_visibility

@dataclass
class Dashboard_PatchRequestBody(Parsable):
    # The expected_revision property
    expected_revision: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The visibility property
    visibility: Optional[Dashboard_PatchRequestBody_visibility] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Dashboard_PatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Dashboard_PatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Dashboard_PatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dashboard_patch_request_body_visibility import Dashboard_PatchRequestBody_visibility

        from .dashboard_patch_request_body_visibility import Dashboard_PatchRequestBody_visibility

        fields: dict[str, Callable[[Any], None]] = {
            "expected_revision": lambda n : setattr(self, 'expected_revision', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(Dashboard_PatchRequestBody_visibility)),
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
        writer.write_int_value("expected_revision", self.expected_revision)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("visibility", self.visibility)
    

