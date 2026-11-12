from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..protobuf.any import Any

@dataclass
class Status(APIError, AdditionalDataHolder, Parsable):
    """
    The Status type defines a logical error model suitable for gRPC and REST APIs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The status code, which should be an enum value of google.rpc.Code.
    code: Optional[int] = None
    # A list of messages that carry the error details.
    details: Optional[list[Any]] = None
    # A developer-facing error message.
    message: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Status:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Status
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Status()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..protobuf.any import Any

        from ..protobuf.any import Any

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_int_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(Any)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
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
        writer.write_int_value("code", self.code)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_str_value("message", self.message)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

