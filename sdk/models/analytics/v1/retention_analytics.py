from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .retention_cohort import RetentionCohort

@dataclass
class RetentionAnalytics(Parsable):
    # The cohorts property
    cohorts: Optional[list[RetentionCohort]] = None
    # The period property
    period: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .retention_cohort import RetentionCohort

        from .retention_cohort import RetentionCohort

        fields: dict[str, Callable[[Any], None]] = {
            "cohorts": lambda n : setattr(self, 'cohorts', n.get_collection_of_object_values(RetentionCohort)),
            "period": lambda n : setattr(self, 'period', n.get_str_value()),
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
        writer.write_collection_of_object_values("cohorts", self.cohorts)
        writer.write_str_value("period", self.period)
    

