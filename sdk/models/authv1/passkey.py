from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Passkey(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The aaguid property
    aaguid: Optional[str] = None
    # The backup_state property
    backup_state: Optional[bool] = None
    # The created_at property
    created_at: Optional[str] = None
    # The credential_id property
    credential_id: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The last_used_at property
    last_used_at: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The transports property
    transports: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Passkey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Passkey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Passkey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "aaguid": lambda n : setattr(self, 'aaguid', n.get_str_value()),
            "backup_state": lambda n : setattr(self, 'backup_state', n.get_bool_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "credential_id": lambda n : setattr(self, 'credential_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "last_used_at": lambda n : setattr(self, 'last_used_at', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "transports": lambda n : setattr(self, 'transports', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("aaguid", self.aaguid)
        writer.write_bool_value("backup_state", self.backup_state)
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("credential_id", self.credential_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("last_used_at", self.last_used_at)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("transports", self.transports)
        writer.write_additional_data_value(self.additional_data)
    

