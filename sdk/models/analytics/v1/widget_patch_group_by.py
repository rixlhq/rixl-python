from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_by import GroupBy
    from .widget_patch_group_by_member1 import WidgetPatch_group_byMember1

@dataclass
class WidgetPatch_group_by(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes GroupBy, WidgetPatch_group_byMember1
    """
    # Composed type representation for type GroupBy
    group_by: Optional[GroupBy] = None
    # Composed type representation for type WidgetPatch_group_byMember1
    widget_patch_group_by_member1: Optional[WidgetPatch_group_byMember1] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WidgetPatch_group_by:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WidgetPatch_group_by
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = WidgetPatch_group_by()
        if mapping_value and mapping_value.casefold() == "analytics.v1.GroupBy".casefold():
            from .group_by import GroupBy

            result.group_by = GroupBy()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_by import GroupBy
        from .widget_patch_group_by_member1 import WidgetPatch_group_byMember1

        if self.group_by:
            return self.group_by.get_field_deserializers()
        if self.widget_patch_group_by_member1:
            return self.widget_patch_group_by_member1.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.group_by:
            writer.write_object_value(None, self.group_by)
        elif self.widget_patch_group_by_member1:
            writer.write_object_value(None, self.widget_patch_group_by_member1)
    

