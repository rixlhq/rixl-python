from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .widget import Widget

@dataclass
class Dashboard(Parsable):
    # The created_at property
    created_at: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The is_default property
    is_default: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The owner_user_id property
    owner_user_id: Optional[str] = None
    # The revision property
    revision: Optional[int] = None
    # The updated_at property
    updated_at: Optional[str] = None
    # The updated_by property
    updated_by: Optional[str] = None
    # The visibility property
    visibility: Optional[str] = None
    # The widgets property
    widgets: Optional[list[Widget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Dashboard:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Dashboard
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Dashboard()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .widget import Widget

        from .widget import Widget

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "owner_user_id": lambda n : setattr(self, 'owner_user_id', n.get_str_value()),
            "revision": lambda n : setattr(self, 'revision', n.get_int_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_str_value()),
            "updated_by": lambda n : setattr(self, 'updated_by', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
            "widgets": lambda n : setattr(self, 'widgets', n.get_collection_of_object_values(Widget)),
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
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("is_default", self.is_default)
        writer.write_str_value("name", self.name)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("owner_user_id", self.owner_user_id)
        writer.write_int_value("revision", self.revision)
        writer.write_str_value("updated_at", self.updated_at)
        writer.write_str_value("updated_by", self.updated_by)
        writer.write_str_value("visibility", self.visibility)
        writer.write_collection_of_object_values("widgets", self.widgets)
    

