from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .funnel_step_filters import FunnelStep_filters

@dataclass
class FunnelStep(Parsable):
    # The event_type property
    event_type: Optional[str] = None
    # The filters property
    filters: Optional[FunnelStep_filters] = None
    # The name property
    name: Optional[str] = None
    # The page_type property
    page_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FunnelStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FunnelStep
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FunnelStep()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .funnel_step_filters import FunnelStep_filters

        from .funnel_step_filters import FunnelStep_filters

        fields: dict[str, Callable[[Any], None]] = {
            "event_type": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "filters": lambda n : setattr(self, 'filters', n.get_object_value(FunnelStep_filters)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "page_type": lambda n : setattr(self, 'page_type', n.get_str_value()),
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
        writer.write_str_value("event_type", self.event_type)
        writer.write_object_value("filters", self.filters)
        writer.write_str_value("name", self.name)
        writer.write_str_value("page_type", self.page_type)
    

