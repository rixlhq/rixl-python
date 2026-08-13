from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_option import FilterOption

@dataclass
class GetFilterOptionsResponse(Parsable):
    # The options property
    options: Optional[list[FilterOption]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetFilterOptionsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetFilterOptionsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetFilterOptionsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_option import FilterOption

        from .filter_option import FilterOption

        fields: dict[str, Callable[[Any], None]] = {
            "options": lambda n : setattr(self, 'options', n.get_collection_of_object_values(FilterOption)),
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
        writer.write_collection_of_object_values("options", self.options)
    

