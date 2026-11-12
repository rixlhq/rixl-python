from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .auto_join_put_request_body_user import AutoJoinPutRequestBody_user

@dataclass
class AutoJoinPutRequestBody(Parsable):
    # The enabled property
    enabled: Optional[bool] = None
    # The user property
    user: Optional[AutoJoinPutRequestBody_user] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutoJoinPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutoJoinPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutoJoinPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .auto_join_put_request_body_user import AutoJoinPutRequestBody_user

        from .auto_join_put_request_body_user import AutoJoinPutRequestBody_user

        fields: dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(AutoJoinPutRequestBody_user)),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_object_value("user", self.user)
    

