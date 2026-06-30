from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StorageUsage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The image_file_count property
    image_file_count: Optional[int] = None
    # The image_storage_bytes property
    image_storage_bytes: Optional[int] = None
    # The last_updated property
    last_updated: Optional[str] = None
    # The max_image_count property
    max_image_count: Optional[int] = None
    # The max_project_count property
    max_project_count: Optional[int] = None
    # The max_video_count property
    max_video_count: Optional[int] = None
    # The org_id property
    org_id: Optional[str] = None
    # The project_count property
    project_count: Optional[int] = None
    # The snapshot_date property
    snapshot_date: Optional[str] = None
    # The total_file_count property
    total_file_count: Optional[int] = None
    # The total_storage_bytes property
    total_storage_bytes: Optional[int] = None
    # The total_video_minutes property
    total_video_minutes: Optional[str] = None
    # The video_file_count property
    video_file_count: Optional[int] = None
    # The video_storage_bytes property
    video_storage_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StorageUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "image_file_count": lambda n : setattr(self, 'image_file_count', n.get_int_value()),
            "image_storage_bytes": lambda n : setattr(self, 'image_storage_bytes', n.get_int_value()),
            "last_updated": lambda n : setattr(self, 'last_updated', n.get_str_value()),
            "max_image_count": lambda n : setattr(self, 'max_image_count', n.get_int_value()),
            "max_project_count": lambda n : setattr(self, 'max_project_count', n.get_int_value()),
            "max_video_count": lambda n : setattr(self, 'max_video_count', n.get_int_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "project_count": lambda n : setattr(self, 'project_count', n.get_int_value()),
            "snapshot_date": lambda n : setattr(self, 'snapshot_date', n.get_str_value()),
            "total_file_count": lambda n : setattr(self, 'total_file_count', n.get_int_value()),
            "total_storage_bytes": lambda n : setattr(self, 'total_storage_bytes', n.get_int_value()),
            "total_video_minutes": lambda n : setattr(self, 'total_video_minutes', n.get_str_value()),
            "video_file_count": lambda n : setattr(self, 'video_file_count', n.get_int_value()),
            "video_storage_bytes": lambda n : setattr(self, 'video_storage_bytes', n.get_int_value()),
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
        writer.write_int_value("image_file_count", self.image_file_count)
        writer.write_int_value("image_storage_bytes", self.image_storage_bytes)
        writer.write_str_value("last_updated", self.last_updated)
        writer.write_int_value("max_image_count", self.max_image_count)
        writer.write_int_value("max_project_count", self.max_project_count)
        writer.write_int_value("max_video_count", self.max_video_count)
        writer.write_str_value("org_id", self.org_id)
        writer.write_int_value("project_count", self.project_count)
        writer.write_str_value("snapshot_date", self.snapshot_date)
        writer.write_int_value("total_file_count", self.total_file_count)
        writer.write_int_value("total_storage_bytes", self.total_storage_bytes)
        writer.write_str_value("total_video_minutes", self.total_video_minutes)
        writer.write_int_value("video_file_count", self.video_file_count)
        writer.write_int_value("video_storage_bytes", self.video_storage_bytes)
        writer.write_additional_data_value(self.additional_data)
    

