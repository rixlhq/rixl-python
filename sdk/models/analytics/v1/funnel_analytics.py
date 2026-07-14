from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .funnel_step_result import FunnelStepResult

@dataclass
class FunnelAnalytics(Parsable):
    # The averageTimeHours property
    average_time_hours: Optional[float] = None
    # The completedUsers property
    completed_users: Optional[int] = None
    # The completionRate property
    completion_rate: Optional[float] = None
    # The steps property
    steps: Optional[list[FunnelStepResult]] = None
    # The totalUsers property
    total_users: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FunnelAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FunnelAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FunnelAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .funnel_step_result import FunnelStepResult

        from .funnel_step_result import FunnelStepResult

        fields: dict[str, Callable[[Any], None]] = {
            "averageTimeHours": lambda n : setattr(self, 'average_time_hours', n.get_float_value()),
            "completedUsers": lambda n : setattr(self, 'completed_users', n.get_int_value()),
            "completionRate": lambda n : setattr(self, 'completion_rate', n.get_float_value()),
            "steps": lambda n : setattr(self, 'steps', n.get_collection_of_object_values(FunnelStepResult)),
            "totalUsers": lambda n : setattr(self, 'total_users', n.get_int_value()),
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
        writer.write_float_value("averageTimeHours", self.average_time_hours)
        writer.write_int_value("completedUsers", self.completed_users)
        writer.write_float_value("completionRate", self.completion_rate)
        writer.write_collection_of_object_values("steps", self.steps)
        writer.write_int_value("totalUsers", self.total_users)
    

