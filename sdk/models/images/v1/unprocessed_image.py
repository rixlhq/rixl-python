from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...common.v1.file_status import FileStatus

@dataclass
class UnprocessedImage(Parsable):
    # The format property
    format: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    # The s3_path property
    s3_path: Optional[str] = None
    # The status property
    status: Optional[FileStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnprocessedImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnprocessedImage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnprocessedImage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...common.v1.file_status import FileStatus

        from ...common.v1.file_status import FileStatus

        fields: dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "s3_path": lambda n : setattr(self, 's3_path', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FileStatus)),
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
        writer.write_str_value("format", self.format)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("project_id", self.project_id)
        writer.write_str_value("s3_path", self.s3_path)
        writer.write_enum_value("status", self.status)
    

