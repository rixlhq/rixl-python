from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_client_credential_request_alg import CreateClientCredentialRequest_alg

@dataclass
class CreateClientCredentialRequest(Parsable):
    # The alg property
    alg: Optional[CreateClientCredentialRequest_alg] = None
    # The name property
    name: Optional[str] = None
    # The orgId property
    org_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateClientCredentialRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateClientCredentialRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateClientCredentialRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .create_client_credential_request_alg import CreateClientCredentialRequest_alg

        from .create_client_credential_request_alg import CreateClientCredentialRequest_alg

        fields: dict[str, Callable[[Any], None]] = {
            "alg": lambda n : setattr(self, 'alg', n.get_enum_value(CreateClientCredentialRequest_alg)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "orgId": lambda n : setattr(self, 'org_id', n.get_str_value()),
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
        writer.write_enum_value("alg", self.alg)
        writer.write_str_value("name", self.name)
        writer.write_str_value("orgId", self.org_id)
    

