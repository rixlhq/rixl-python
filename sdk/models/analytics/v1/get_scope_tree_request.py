from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .get_scope_tree_request_level import GetScopeTreeRequest_level
    from .get_scope_tree_request_resource_type import GetScopeTreeRequest_resource_type

@dataclass
class GetScopeTreeRequest(Parsable):
    # Which level to expand. Empty returns the projects at the root.
    level: Optional[GetScopeTreeRequest_level] = None
    # The limit property
    limit: Optional[int] = None
    # The project_id property
    project_id: Optional[str] = None
    # The resource_type property
    resource_type: Optional[GetScopeTreeRequest_resource_type] = None
    # The search property
    search: Optional[str] = None
    # The time_end property
    time_end: Optional[str] = None
    # The time_start property
    time_start: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetScopeTreeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetScopeTreeRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetScopeTreeRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .get_scope_tree_request_level import GetScopeTreeRequest_level
        from .get_scope_tree_request_resource_type import GetScopeTreeRequest_resource_type

        from .get_scope_tree_request_level import GetScopeTreeRequest_level
        from .get_scope_tree_request_resource_type import GetScopeTreeRequest_resource_type

        fields: dict[str, Callable[[Any], None]] = {
            "level": lambda n : setattr(self, 'level', n.get_enum_value(GetScopeTreeRequest_level)),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "resource_type": lambda n : setattr(self, 'resource_type', n.get_enum_value(GetScopeTreeRequest_resource_type)),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "time_end": lambda n : setattr(self, 'time_end', n.get_str_value()),
            "time_start": lambda n : setattr(self, 'time_start', n.get_str_value()),
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
        writer.write_enum_value("level", self.level)
        writer.write_int_value("limit", self.limit)
        writer.write_str_value("project_id", self.project_id)
        writer.write_enum_value("resource_type", self.resource_type)
        writer.write_str_value("search", self.search)
        writer.write_str_value("time_end", self.time_end)
        writer.write_str_value("time_start", self.time_start)
    

