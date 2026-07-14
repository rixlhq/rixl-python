from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .invoice import Invoice

@dataclass
class ListInvoicesResponse(Parsable):
    # The invoices property
    invoices: Optional[list[Invoice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListInvoicesResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListInvoicesResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListInvoicesResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .invoice import Invoice

        from .invoice import Invoice

        fields: dict[str, Callable[[Any], None]] = {
            "invoices": lambda n : setattr(self, 'invoices', n.get_collection_of_object_values(Invoice)),
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
        writer.write_collection_of_object_values("invoices", self.invoices)
    

