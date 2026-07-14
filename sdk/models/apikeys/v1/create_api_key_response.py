from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_key import ApiKey

@dataclass
class CreateApiKeyResponse(Parsable):
    # The apiKey property
    api_key: Optional[ApiKey] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateApiKeyResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateApiKeyResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateApiKeyResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .api_key import ApiKey

        from .api_key import ApiKey

        fields: dict[str, Callable[[Any], None]] = {
            "apiKey": lambda n : setattr(self, 'api_key', n.get_object_value(ApiKey)),
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
        writer.write_object_value("apiKey", self.api_key)
    

