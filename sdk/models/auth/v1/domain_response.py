from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_status import DomainStatus

@dataclass
class DomainResponse(Parsable):
    # The domain property
    domain: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The present property
    present: Optional[bool] = None
    # The status property
    status: Optional[DomainStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .domain_status import DomainStatus

        from .domain_status import DomainStatus

        fields: dict[str, Callable[[Any], None]] = {
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "present": lambda n : setattr(self, 'present', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(DomainStatus)),
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
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("present", self.present)
        writer.write_object_value("status", self.status)
    

