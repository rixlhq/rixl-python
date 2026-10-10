from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ApiKey(Parsable):
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The expiring_at property
    expiring_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The last_used property
    last_used: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The permissions property
    permissions: Optional[list[str]] = None
    # The policy_ids property
    policy_ids: Optional[list[str]] = None
    # The project_id property
    project_id: Optional[str] = None
    # The project_name property
    project_name: Optional[str] = None
    # The secret property
    secret: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApiKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApiKey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApiKey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "expiring_at": lambda n : setattr(self, 'expiring_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "last_used": lambda n : setattr(self, 'last_used', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "policy_ids": lambda n : setattr(self, 'policy_ids', n.get_collection_of_primitive_values(str)),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "project_name": lambda n : setattr(self, 'project_name', n.get_str_value()),
            "secret": lambda n : setattr(self, 'secret', n.get_str_value()),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_datetime_value("expiring_at", self.expiring_at)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("last_used", self.last_used)
        writer.write_str_value("name", self.name)
        writer.write_str_value("org_id", self.org_id)
        writer.write_collection_of_primitive_values("permissions", self.permissions)
        writer.write_collection_of_primitive_values("policy_ids", self.policy_ids)
        writer.write_str_value("project_id", self.project_id)
        writer.write_str_value("project_name", self.project_name)
        writer.write_str_value("secret", self.secret)
    

