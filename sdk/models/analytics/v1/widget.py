from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chart_filter import ChartFilter

@dataclass
class Widget(Parsable):
    # The chart_type property
    chart_type: Optional[str] = None
    # The created_at property
    created_at: Optional[str] = None
    # The dashboard_id property
    dashboard_id: Optional[str] = None
    # The dashboard_revision property
    dashboard_revision: Optional[int] = None
    # The dataset property
    dataset: Optional[str] = None
    # The filters property
    filters: Optional[list[ChartFilter]] = None
    # The group_by property
    group_by: Optional[list[str]] = None
    # The height property
    height: Optional[int] = None
    # The id property
    id: Optional[str] = None
    # The interval property
    interval: Optional[str] = None
    # The limit property
    limit: Optional[int] = None
    # The metric property
    metric: Optional[str] = None
    # The pos_x property
    pos_x: Optional[int] = None
    # The pos_y property
    pos_y: Optional[int] = None
    # The sort_order property
    sort_order: Optional[int] = None
    # The spec_version property
    spec_version: Optional[int] = None
    # The title property
    title: Optional[str] = None
    # The updated_at property
    updated_at: Optional[str] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Widget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Widget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Widget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chart_filter import ChartFilter

        from .chart_filter import ChartFilter

        fields: dict[str, Callable[[Any], None]] = {
            "chart_type": lambda n : setattr(self, 'chart_type', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "dashboard_id": lambda n : setattr(self, 'dashboard_id', n.get_str_value()),
            "dashboard_revision": lambda n : setattr(self, 'dashboard_revision', n.get_int_value()),
            "dataset": lambda n : setattr(self, 'dataset', n.get_str_value()),
            "filters": lambda n : setattr(self, 'filters', n.get_collection_of_object_values(ChartFilter)),
            "group_by": lambda n : setattr(self, 'group_by', n.get_collection_of_primitive_values(str)),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "interval": lambda n : setattr(self, 'interval', n.get_str_value()),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "metric": lambda n : setattr(self, 'metric', n.get_str_value()),
            "pos_x": lambda n : setattr(self, 'pos_x', n.get_int_value()),
            "pos_y": lambda n : setattr(self, 'pos_y', n.get_int_value()),
            "sort_order": lambda n : setattr(self, 'sort_order', n.get_int_value()),
            "spec_version": lambda n : setattr(self, 'spec_version', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("dashboard_id", self.dashboard_id)
        writer.write_int_value("dashboard_revision", self.dashboard_revision)
        writer.write_str_value("dataset", self.dataset)
        writer.write_collection_of_object_values("filters", self.filters)
        writer.write_collection_of_primitive_values("group_by", self.group_by)
        writer.write_int_value("height", self.height)
        writer.write_str_value("id", self.id)
        writer.write_str_value("interval", self.interval)
        writer.write_int_value("limit", self.limit)
        writer.write_str_value("metric", self.metric)
        writer.write_int_value("pos_x", self.pos_x)
        writer.write_int_value("pos_y", self.pos_y)
        writer.write_int_value("sort_order", self.sort_order)
        writer.write_int_value("spec_version", self.spec_version)
        writer.write_str_value("title", self.title)
        writer.write_str_value("updated_at", self.updated_at)
        writer.write_int_value("width", self.width)
    

