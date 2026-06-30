from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DomainResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The auto_join property
    auto_join: Optional[bool] = None
    # The domain property
    domain: Optional[str] = None
    # The expires_at property
    expires_at: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The message property
    message: Optional[str] = None
    # The present property
    present: Optional[bool] = None
    # The status property
    status: Optional[str] = None
    # The verification_token property
    verification_token: Optional[str] = None
    # The verified_at property
    verified_at: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "auto_join": lambda n : setattr(self, 'auto_join', n.get_bool_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "present": lambda n : setattr(self, 'present', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "verification_token": lambda n : setattr(self, 'verification_token', n.get_str_value()),
            "verified_at": lambda n : setattr(self, 'verified_at', n.get_str_value()),
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
        writer.write_bool_value("auto_join", self.auto_join)
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("expires_at", self.expires_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("message", self.message)
        writer.write_bool_value("present", self.present)
        writer.write_str_value("status", self.status)
        writer.write_str_value("verification_token", self.verification_token)
        writer.write_str_value("verified_at", self.verified_at)
        writer.write_additional_data_value(self.additional_data)
    

