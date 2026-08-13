from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GetFilterOptionsRequest(Parsable):
    # The dataset property
    dataset: Optional[str] = None
    # The field property
    field: Optional[str] = None
    # The limit property
    limit: Optional[int] = None
    # The time_end property
    time_end: Optional[str] = None
    # The time_start property
    time_start: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetFilterOptionsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetFilterOptionsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetFilterOptionsRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "dataset": lambda n : setattr(self, 'dataset', n.get_str_value()),
            "field": lambda n : setattr(self, 'field', n.get_str_value()),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "time_end": lambda n : setattr(self, 'time_end', n.get_str_value()),
            "time_start": lambda n : setattr(self, 'time_start', n.get_str_value()),
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
        writer.write_str_value("dataset", self.dataset)
        writer.write_str_value("field", self.field)
        writer.write_int_value("limit", self.limit)
        writer.write_str_value("time_end", self.time_end)
        writer.write_str_value("time_start", self.time_start)
    

