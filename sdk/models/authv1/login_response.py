from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LoginResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The access_token property
    access_token: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The expires_in property
    expires_in: Optional[int] = None
    # The refresh_token property
    refresh_token: Optional[str] = None
    # The requires_action property
    requires_action: Optional[str] = None
    # The session_id property
    session_id: Optional[str] = None
    # "ok" | "otp_required" | "email_not_verified"
    status: Optional[str] = None
    # The token_type property
    token_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoginResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoginResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoginResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "access_token": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expires_in": lambda n : setattr(self, 'expires_in', n.get_int_value()),
            "refresh_token": lambda n : setattr(self, 'refresh_token', n.get_str_value()),
            "requires_action": lambda n : setattr(self, 'requires_action', n.get_str_value()),
            "session_id": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("access_token", self.access_token)
        writer.write_str_value("email", self.email)
        writer.write_int_value("expires_in", self.expires_in)
        writer.write_str_value("refresh_token", self.refresh_token)
        writer.write_str_value("requires_action", self.requires_action)
        writer.write_str_value("session_id", self.session_id)
        writer.write_str_value("status", self.status)
        writer.write_str_value("token_type", self.token_type)
        writer.write_additional_data_value(self.additional_data)
    

