from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.auth.v1.user_org_request import UserOrgRequest

@dataclass
class WithPolicy_PutRequestBody(Parsable):
    # The description property
    description: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The permissions property
    permissions: Optional[list[str]] = None
    # The user property
    user: Optional[UserOrgRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithPolicy_PutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithPolicy_PutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithPolicy_PutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.auth.v1.user_org_request import UserOrgRequest

        from .......models.auth.v1.user_org_request import UserOrgRequest

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(UserOrgRequest)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("permissions", self.permissions)
        writer.write_object_value("user", self.user)
    

