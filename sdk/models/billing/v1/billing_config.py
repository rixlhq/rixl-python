from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BillingConfig(Parsable):
    # Stripe publishable key of the account the caller's organization is billed in.
    publishable_key: Optional[str] = None
    # True when the organization is billed in the Stripe sandbox: no money moves.
    sandbox: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BillingConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BillingConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BillingConfig()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "publishable_key": lambda n : setattr(self, 'publishable_key', n.get_str_value()),
            "sandbox": lambda n : setattr(self, 'sandbox', n.get_bool_value()),
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
        writer.write_str_value("publishable_key", self.publishable_key)
        writer.write_bool_value("sandbox", self.sandbox)
    

