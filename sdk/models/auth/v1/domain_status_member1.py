from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pending_domain import PendingDomain

@dataclass
class DomainStatusMember1(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The pending property
    pending: Optional[PendingDomain] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainStatusMember1:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainStatusMember1
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainStatusMember1()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pending_domain import PendingDomain

        from .pending_domain import PendingDomain

        fields: dict[str, Callable[[Any], None]] = {
            "pending": lambda n : setattr(self, 'pending', n.get_object_value(PendingDomain)),
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
        writer.write_object_value("pending", self.pending)
        writer.write_additional_data_value(self.additional_data)
    

