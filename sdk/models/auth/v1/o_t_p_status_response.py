from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OTPStatusResponse(Parsable):
    # The backup_codes_remaining property
    backup_codes_remaining: Optional[int] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The is_setup property
    is_setup: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OTPStatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OTPStatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OTPStatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "backup_codes_remaining": lambda n : setattr(self, 'backup_codes_remaining', n.get_int_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "is_setup": lambda n : setattr(self, 'is_setup', n.get_bool_value()),
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
        writer.write_int_value("backup_codes_remaining", self.backup_codes_remaining)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_bool_value("is_setup", self.is_setup)
    

