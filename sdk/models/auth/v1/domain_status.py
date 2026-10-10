from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_status_member1 import DomainStatusMember1
    from .domain_status_member2 import DomainStatusMember2

@dataclass
class DomainStatus(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes DomainStatusMember1, DomainStatusMember2
    """
    # Composed type representation for type DomainStatusMember1
    domain_status_member1: Optional[DomainStatusMember1] = None
    # Composed type representation for type DomainStatusMember2
    domain_status_member2: Optional[DomainStatusMember2] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = DomainStatus()
        from .domain_status_member1 import DomainStatusMember1

        result.domain_status_member1 = DomainStatusMember1()
        from .domain_status_member2 import DomainStatusMember2

        result.domain_status_member2 = DomainStatusMember2()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .domain_status_member1 import DomainStatusMember1
        from .domain_status_member2 import DomainStatusMember2

        if self.domain_status_member1 or self.domain_status_member2:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.domain_status_member1, self.domain_status_member2)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value(None, self.domain_status_member1, self.domain_status_member2)
    

