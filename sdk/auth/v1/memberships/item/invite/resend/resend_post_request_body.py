from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.auth.v1.actor_org_request import ActorOrgRequest

@dataclass
class ResendPostRequestBody(Parsable):
    # The user property
    user: Optional[ActorOrgRequest] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResendPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResendPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResendPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.auth.v1.actor_org_request import ActorOrgRequest

        from .......models.auth.v1.actor_org_request import ActorOrgRequest

        fields: dict[str, Callable[[Any], None]] = {
            "user": lambda n : setattr(self, 'user', n.get_object_value(ActorOrgRequest)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("user", self.user)
        writer.write_str_value("userId", self.user_id)
    

