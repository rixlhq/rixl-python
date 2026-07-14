from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .project import Project

@dataclass
class ListProjectsResponse(Parsable):
    # The projects property
    projects: Optional[list[Project]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListProjectsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListProjectsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListProjectsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .project import Project

        from .project import Project

        fields: dict[str, Callable[[Any], None]] = {
            "projects": lambda n : setattr(self, 'projects', n.get_collection_of_object_values(Project)),
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
        writer.write_collection_of_object_values("projects", self.projects)
    

