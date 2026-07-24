from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class HotSegment(Parsable):
    # The end_second property
    end_second: Optional[int] = None
    # The multiplier property
    multiplier: Optional[float] = None
    # The start_second property
    start_second: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HotSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HotSegment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HotSegment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "end_second": lambda n : setattr(self, 'end_second', n.get_int_value()),
            "multiplier": lambda n : setattr(self, 'multiplier', n.get_float_value()),
            "start_second": lambda n : setattr(self, 'start_second', n.get_int_value()),
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
        writer.write_int_value("end_second", self.end_second)
        writer.write_float_value("multiplier", self.multiplier)
        writer.write_int_value("start_second", self.start_second)
    

