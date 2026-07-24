from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class VerificationSentResponse(Parsable):
    # The can_resend_at property
    can_resend_at: Optional[str] = None
    # The code_sent property
    code_sent: Optional[bool] = None
    # The message property
    message: Optional[str] = None
    # The verification_id property
    verification_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerificationSentResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerificationSentResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerificationSentResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "can_resend_at": lambda n : setattr(self, 'can_resend_at', n.get_str_value()),
            "code_sent": lambda n : setattr(self, 'code_sent', n.get_bool_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "verification_id": lambda n : setattr(self, 'verification_id', n.get_str_value()),
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
        writer.write_str_value("can_resend_at", self.can_resend_at)
        writer.write_bool_value("code_sent", self.code_sent)
        writer.write_str_value("message", self.message)
        writer.write_str_value("verification_id", self.verification_id)
    

