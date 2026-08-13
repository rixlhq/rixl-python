from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dataset_field import DatasetField
    from .dataset_metric import DatasetMetric

@dataclass
class Dataset(Parsable):
    # The dimensions property
    dimensions: Optional[list[DatasetField]] = None
    # The filters property
    filters: Optional[list[DatasetField]] = None
    # The id property
    id: Optional[str] = None
    # The label property
    label: Optional[str] = None
    # The metrics property
    metrics: Optional[list[DatasetMetric]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Dataset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Dataset
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Dataset()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dataset_field import DatasetField
        from .dataset_metric import DatasetMetric

        from .dataset_field import DatasetField
        from .dataset_metric import DatasetMetric

        fields: dict[str, Callable[[Any], None]] = {
            "dimensions": lambda n : setattr(self, 'dimensions', n.get_collection_of_object_values(DatasetField)),
            "filters": lambda n : setattr(self, 'filters', n.get_collection_of_object_values(DatasetField)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "metrics": lambda n : setattr(self, 'metrics', n.get_collection_of_object_values(DatasetMetric)),
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
        writer.write_collection_of_object_values("dimensions", self.dimensions)
        writer.write_collection_of_object_values("filters", self.filters)
        writer.write_str_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_collection_of_object_values("metrics", self.metrics)
    

