from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RetentionCohort(Parsable):
    # The cohortDate property
    cohort_date: Optional[str] = None
    # The cohortSize property
    cohort_size: Optional[int] = None
    # The retentionData property
    retention_data: Optional[list[float]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionCohort:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionCohort
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionCohort()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cohortDate": lambda n : setattr(self, 'cohort_date', n.get_str_value()),
            "cohortSize": lambda n : setattr(self, 'cohort_size', n.get_int_value()),
            "retentionData": lambda n : setattr(self, 'retention_data', n.get_collection_of_primitive_values(float)),
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
        writer.write_str_value("cohortDate", self.cohort_date)
        writer.write_int_value("cohortSize", self.cohort_size)
        writer.write_collection_of_primitive_values("retentionData", self.retention_data)
    

