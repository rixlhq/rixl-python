from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.analytics.v1.widget_patch import WidgetPatch

@dataclass
class WidgetsPatchRequestBody(Parsable):
    # The expected_revision property
    expected_revision: Optional[int] = None
    # The patch property
    patch: Optional[WidgetPatch] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WidgetsPatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WidgetsPatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WidgetsPatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.analytics.v1.widget_patch import WidgetPatch

        from ......models.analytics.v1.widget_patch import WidgetPatch

        fields: dict[str, Callable[[Any], None]] = {
            "expected_revision": lambda n : setattr(self, 'expected_revision', n.get_int_value()),
            "patch": lambda n : setattr(self, 'patch', n.get_object_value(WidgetPatch)),
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
        writer.write_object_value("patch", self.patch)
    

