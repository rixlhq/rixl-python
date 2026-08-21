from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chart_filter import ChartFilter

@dataclass
class ScopeNode(Parsable):
    # The filters property
    filters: Optional[list[ChartFilter]] = None
    # The has_children property
    has_children: Optional[bool] = None
    # The id property
    id: Optional[str] = None
    # The kind property
    kind: Optional[str] = None
    # The label property
    label: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScopeNode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScopeNode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScopeNode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chart_filter import ChartFilter

        from .chart_filter import ChartFilter

        fields: dict[str, Callable[[Any], None]] = {
            "filters": lambda n : setattr(self, 'filters', n.get_collection_of_object_values(ChartFilter)),
            "has_children": lambda n : setattr(self, 'has_children', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
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
        writer.write_collection_of_object_values("filters", self.filters)
        writer.write_bool_value("has_children", self.has_children)
        writer.write_str_value("id", self.id)
        writer.write_str_value("kind", self.kind)
        writer.write_str_value("label", self.label)
    

