from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connected_provider import ConnectedProvider

@dataclass
class ListProvidersResponse(Parsable):
    # The providers property
    providers: Optional[list[ConnectedProvider]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListProvidersResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListProvidersResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListProvidersResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connected_provider import ConnectedProvider

        from .connected_provider import ConnectedProvider

        fields: dict[str, Callable[[Any], None]] = {
            "providers": lambda n : setattr(self, 'providers', n.get_collection_of_object_values(ConnectedProvider)),
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
        writer.write_collection_of_object_values("providers", self.providers)
    

