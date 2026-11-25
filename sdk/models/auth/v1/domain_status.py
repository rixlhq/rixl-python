from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pending_domain import PendingDomain
    from .verified_domain import VerifiedDomain

@dataclass
class DomainStatus(Parsable):
    """
    At most one of `verified`, `pending` may be set.
    """
    # The pending property
    pending: Optional[PendingDomain] = None
    # The suggest_join property
    suggest_join: Optional[bool] = None
    # The verified property
    verified: Optional[VerifiedDomain] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pending_domain import PendingDomain
        from .verified_domain import VerifiedDomain

        from .pending_domain import PendingDomain
        from .verified_domain import VerifiedDomain

        fields: dict[str, Callable[[Any], None]] = {
            "pending": lambda n : setattr(self, 'pending', n.get_object_value(PendingDomain)),
            "suggest_join": lambda n : setattr(self, 'suggest_join', n.get_bool_value()),
            "verified": lambda n : setattr(self, 'verified', n.get_object_value(VerifiedDomain)),
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
        writer.write_bool_value("suggest_join", self.suggest_join)
        writer.write_object_value("verified", self.verified)
    

