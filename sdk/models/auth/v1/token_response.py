from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization import Organization

@dataclass
class TokenResponse(Parsable):
    # The access_token property
    access_token: Optional[str] = None
    # The domain_join_suggestions property
    domain_join_suggestions: Optional[list[Organization]] = None
    # The expires_in property
    expires_in: Optional[str] = None
    # The last_active_org_id property
    last_active_org_id: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The refresh_token property
    refresh_token: Optional[str] = None
    # The requires_action property
    requires_action: Optional[str] = None
    # The role property
    role: Optional[str] = None
    # The token_type property
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
        from .organization import Organization

        from .organization import Organization

        fields: dict[str, Callable[[Any], None]] = {
            "access_token": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "domain_join_suggestions": lambda n : setattr(self, 'domain_join_suggestions', n.get_collection_of_object_values(Organization)),
            "expires_in": lambda n : setattr(self, 'expires_in', n.get_str_value()),
            "last_active_org_id": lambda n : setattr(self, 'last_active_org_id', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "refresh_token": lambda n : setattr(self, 'refresh_token', n.get_str_value()),
            "requires_action": lambda n : setattr(self, 'requires_action', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
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
        writer.write_collection_of_object_values("domain_join_suggestions", self.domain_join_suggestions)
        writer.write_str_value("expires_in", self.expires_in)
        writer.write_str_value("last_active_org_id", self.last_active_org_id)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("refresh_token", self.refresh_token)
        writer.write_str_value("requires_action", self.requires_action)
        writer.write_str_value("role", self.role)
        writer.write_str_value("token_type", self.token_type)
    

