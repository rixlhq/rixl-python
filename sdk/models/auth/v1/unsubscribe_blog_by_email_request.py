from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_request import UserRequest

@dataclass
class UnsubscribeBlogByEmailRequest(Parsable):
    # The email property
    email: Optional[str] = None
    # The user property
    user: Optional[UserRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnsubscribeBlogByEmailRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnsubscribeBlogByEmailRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnsubscribeBlogByEmailRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_request import UserRequest

        from .user_request import UserRequest

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(UserRequest)),
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
        writer.write_str_value("email", self.email)
        writer.write_object_value("user", self.user)
    

