from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .widget_patch_filters import WidgetPatch_filters
    from .widget_patch_group_by import WidgetPatch_group_by

@dataclass
class WidgetPatch(Parsable):
    # The chart_type property
    chart_type: Optional[str] = None
    # The dataset property
    dataset: Optional[str] = None
    # The filters property
    filters: Optional[WidgetPatch_filters] = None
    # The group_by property
    group_by: Optional[WidgetPatch_group_by] = None
    # The interval property
    interval: Optional[str] = None
    # The limit property
    limit: Optional[int] = None
    # The metric property
    metric: Optional[str] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WidgetPatch:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WidgetPatch
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WidgetPatch()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .widget_patch_filters import WidgetPatch_filters
        from .widget_patch_group_by import WidgetPatch_group_by

        from .widget_patch_filters import WidgetPatch_filters
        from .widget_patch_group_by import WidgetPatch_group_by

        fields: dict[str, Callable[[Any], None]] = {
            "chart_type": lambda n : setattr(self, 'chart_type', n.get_str_value()),
            "dataset": lambda n : setattr(self, 'dataset', n.get_str_value()),
            "filters": lambda n : setattr(self, 'filters', n.get_object_value(WidgetPatch_filters)),
            "group_by": lambda n : setattr(self, 'group_by', n.get_object_value(WidgetPatch_group_by)),
            "interval": lambda n : setattr(self, 'interval', n.get_str_value()),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "metric": lambda n : setattr(self, 'metric', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("chart_type", self.chart_type)
        writer.write_str_value("dataset", self.dataset)
        writer.write_object_value("filters", self.filters)
        writer.write_object_value("group_by", self.group_by)
        writer.write_str_value("interval", self.interval)
        writer.write_int_value("limit", self.limit)
        writer.write_str_value("metric", self.metric)
        writer.write_str_value("title", self.title)
    

