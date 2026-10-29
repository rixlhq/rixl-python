from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WebhookEndpoint(Parsable):
    """
    WebhookEndpoint is a delivery target. Secrets are never returned; they are only shown once on create and rotate.
    """
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The disabled_reason property
    disabled_reason: Optional[str] = None
    # The enabled property
    enabled: Optional[bool] = None
    # The event_types property
    event_types: Optional[list[str]] = None
    # The id property
    id: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebhookEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebhookEndpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebhookEndpoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "disabled_reason": lambda n : setattr(self, 'disabled_reason', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "event_types": lambda n : setattr(self, 'event_types', n.get_collection_of_primitive_values(str)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("disabled_reason", self.disabled_reason)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_collection_of_primitive_values("event_types", self.event_types)
        writer.write_str_value("id", self.id)
        writer.write_str_value("project_id", self.project_id)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_str_value("url", self.url)
    

