from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PendingDomain(Parsable):
    # The expires_at property
    expires_at: Optional[datetime.datetime] = None
    # The verification_token property
    verification_token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PendingDomain:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PendingDomain
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PendingDomain()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "verification_token": lambda n : setattr(self, 'verification_token', n.get_str_value()),
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
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_str_value("verification_token", self.verification_token)
    

