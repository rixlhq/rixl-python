from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filters import Filters
    from .widget_patch_filters_member1 import WidgetPatch_filtersMember1

@dataclass
class WidgetPatch_filters(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes Filters, WidgetPatch_filtersMember1
    """
    # Composed type representation for type Filters
    filters: Optional[Filters] = None
    # Composed type representation for type WidgetPatch_filtersMember1
    widget_patch_filters_member1: Optional[WidgetPatch_filtersMember1] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WidgetPatch_filters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WidgetPatch_filters
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = WidgetPatch_filters()
        if mapping_value and mapping_value.casefold() == "analytics.v1.Filters".casefold():
            from .filters import Filters

            result.filters = Filters()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filters import Filters
        from .widget_patch_filters_member1 import WidgetPatch_filtersMember1

        if self.filters:
            return self.filters.get_field_deserializers()
        if self.widget_patch_filters_member1:
            return self.widget_patch_filters_member1.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.filters:
            writer.write_object_value(None, self.filters)
        elif self.widget_patch_filters_member1:
            writer.write_object_value(None, self.widget_patch_filters_member1)
    

