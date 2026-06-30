from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PasskeyRegisterFinishBody(AdditionalDataHolder, Parsable):
    """
    session_id, name and WebAuthn credential
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The credential property
    credential: Optional[list[int]] = None
    # The name property
    name: Optional[str] = None
    # The session_id property
    session_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasskeyRegisterFinishBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasskeyRegisterFinishBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasskeyRegisterFinishBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "credential": lambda n : setattr(self, 'credential', n.get_collection_of_primitive_values(int)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "session_id": lambda n : setattr(self, 'session_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("credential", self.credential)
        writer.write_str_value("name", self.name)
        writer.write_str_value("session_id", self.session_id)
        writer.write_additional_data_value(self.additional_data)
    

