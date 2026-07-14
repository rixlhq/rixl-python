from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .auth_method import AuthMethod

@dataclass
class LoginResponse(Parsable):
    # The accessToken property
    access_token: Optional[str] = None
    # authentication lists the 2FA methods the user has configured when status is "2fa_required". The public API renders these as lowercase strings: "passkey", "totp".
    authentication: Optional[list[AuthMethod]] = None
    # The email property
    email: Optional[str] = None
    # passkey_options is the WebAuthn PublicKeyCredentialRequestOptions as JSON, present only when "passkey" is one of the authentication methods.
    passkey_options: Optional[bytes] = None
    # The refreshToken property
    refresh_token: Optional[str] = None
    # The requiresAction property
    requires_action: Optional[str] = None
    # The sessionId property
    session_id: Optional[str] = None
    # "ok" | "2fa_required" | "email_not_verified"
    status: Optional[str] = None
    # The tokenType property
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
        from .auth_method import AuthMethod

        from .auth_method import AuthMethod

        fields: dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "authentication": lambda n : setattr(self, 'authentication', n.get_collection_of_enum_values(AuthMethod)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "passkeyOptions": lambda n : setattr(self, 'passkey_options', n.get_bytes_value()),
            "refreshToken": lambda n : setattr(self, 'refresh_token', n.get_str_value()),
            "requiresAction": lambda n : setattr(self, 'requires_action', n.get_str_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_collection_of_enum_values("authentication", self.authentication)
        writer.write_str_value("email", self.email)
        writer.write_bytes_value("passkeyOptions", self.passkey_options)
        writer.write_str_value("refreshToken", self.refresh_token)
        writer.write_str_value("requiresAction", self.requires_action)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_str_value("status", self.status)
        writer.write_str_value("tokenType", self.token_type)
    

