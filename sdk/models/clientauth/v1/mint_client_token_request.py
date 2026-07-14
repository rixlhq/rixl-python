from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MintClientTokenRequest(Parsable):
    # The clientId property
    client_id: Optional[str] = None
    # The clientSecret property
    client_secret: Optional[str] = None
    # The projectId property
    project_id: Optional[str] = None
    # The subject property
    subject: Optional[str] = None
    # The ttlMinutes property
    ttl_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MintClientTokenRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MintClientTokenRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MintClientTokenRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "projectId": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "ttlMinutes": lambda n : setattr(self, 'ttl_minutes', n.get_int_value()),
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
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("projectId", self.project_id)
        writer.write_str_value("subject", self.subject)
        writer.write_int_value("ttlMinutes", self.ttl_minutes)
    

