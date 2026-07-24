from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RefreshTokenRequest(Parsable):
    # The country_code property
    country_code: Optional[str] = None
    # The origin property
    origin: Optional[str] = None
    # The refresh_token property
    refresh_token: Optional[str] = None
    # The token_type property
    token_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RefreshTokenRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RefreshTokenRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RefreshTokenRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "country_code": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_str_value()),
            "refresh_token": lambda n : setattr(self, 'refresh_token', n.get_str_value()),
            "token_type": lambda n : setattr(self, 'token_type', n.get_str_value()),
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
        writer.write_str_value("country_code", self.country_code)
        writer.write_str_value("origin", self.origin)
        writer.write_str_value("refresh_token", self.refresh_token)
        writer.write_str_value("token_type", self.token_type)
    

