from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PasskeyLoginBeginRequest(Parsable):
    """
    options and credential carry the WebAuthn ceremony payloads verbatim as JSON (the browser credential API consumes them as-is), so they are opaque bytes.
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasskeyLoginBeginRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasskeyLoginBeginRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasskeyLoginBeginRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
    

