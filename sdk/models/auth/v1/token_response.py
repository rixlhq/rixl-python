from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TokenResponse(Parsable):
    # The accessToken property
    access_token: Optional[str] = None
    # The refreshToken property
    refresh_token: Optional[str] = None
    # The requiresAction property
    requires_action: Optional[str] = None
    # The tokenType property
    token_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TokenResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TokenResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TokenResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "refreshToken": lambda n : setattr(self, 'refresh_token', n.get_str_value()),
            "requiresAction": lambda n : setattr(self, 'requires_action', n.get_str_value()),
            "tokenType": lambda n : setattr(self, 'token_type', n.get_str_value()),
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
        writer.write_str_value("accessToken", self.access_token)
        writer.write_str_value("refreshToken", self.refresh_token)
        writer.write_str_value("requiresAction", self.requires_action)
        writer.write_str_value("tokenType", self.token_type)
    

