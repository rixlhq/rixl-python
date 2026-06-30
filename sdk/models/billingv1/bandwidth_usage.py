from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BandwidthUsage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[str] = None
    # The data_source property
    data_source: Optional[str] = None
    # The image_bandwidth_bytes property
    image_bandwidth_bytes: Optional[int] = None
    # The image_requests property
    image_requests: Optional[int] = None
    # The org_id property
    org_id: Optional[str] = None
    # The snapshot_date property
    snapshot_date: Optional[str] = None
    # The snapshot_type property
    snapshot_type: Optional[str] = None
    # The total_bandwidth_bytes property
    total_bandwidth_bytes: Optional[int] = None
    # The total_requests property
    total_requests: Optional[int] = None
    # The unique_visitors property
    unique_visitors: Optional[int] = None
    # The video_bandwidth_bytes property
    video_bandwidth_bytes: Optional[int] = None
    # The video_requests property
    video_requests: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BandwidthUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BandwidthUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BandwidthUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "data_source": lambda n : setattr(self, 'data_source', n.get_str_value()),
            "image_bandwidth_bytes": lambda n : setattr(self, 'image_bandwidth_bytes', n.get_int_value()),
            "image_requests": lambda n : setattr(self, 'image_requests', n.get_int_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "snapshot_date": lambda n : setattr(self, 'snapshot_date', n.get_str_value()),
            "snapshot_type": lambda n : setattr(self, 'snapshot_type', n.get_str_value()),
            "total_bandwidth_bytes": lambda n : setattr(self, 'total_bandwidth_bytes', n.get_int_value()),
            "total_requests": lambda n : setattr(self, 'total_requests', n.get_int_value()),
            "unique_visitors": lambda n : setattr(self, 'unique_visitors', n.get_int_value()),
            "video_bandwidth_bytes": lambda n : setattr(self, 'video_bandwidth_bytes', n.get_int_value()),
            "video_requests": lambda n : setattr(self, 'video_requests', n.get_int_value()),
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
        writer.write_str_value("data_source", self.data_source)
        writer.write_int_value("image_bandwidth_bytes", self.image_bandwidth_bytes)
        writer.write_int_value("image_requests", self.image_requests)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("snapshot_date", self.snapshot_date)
        writer.write_str_value("snapshot_type", self.snapshot_type)
        writer.write_int_value("total_bandwidth_bytes", self.total_bandwidth_bytes)
        writer.write_int_value("total_requests", self.total_requests)
        writer.write_int_value("unique_visitors", self.unique_visitors)
        writer.write_int_value("video_bandwidth_bytes", self.video_bandwidth_bytes)
        writer.write_int_value("video_requests", self.video_requests)
        writer.write_additional_data_value(self.additional_data)
    

