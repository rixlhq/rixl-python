from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notification_category import NotificationCategory

@dataclass
class NotificationPreference(Parsable):
    # always_sent lists the notices in this category the caller receives even with email disabled.
    always_sent: Optional[list[str]] = None
    # The category property
    category: Optional[NotificationCategory] = None
    # The email_enabled property
    email_enabled: Optional[bool] = None
    # locked is true when the caller's role cannot disable the category.
    locked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NotificationPreference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotificationPreference
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NotificationPreference()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .notification_category import NotificationCategory

        from .notification_category import NotificationCategory

        fields: dict[str, Callable[[Any], None]] = {
            "always_sent": lambda n : setattr(self, 'always_sent', n.get_collection_of_primitive_values(str)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(NotificationCategory)),
            "email_enabled": lambda n : setattr(self, 'email_enabled', n.get_bool_value()),
            "locked": lambda n : setattr(self, 'locked', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("always_sent", self.always_sent)
        writer.write_enum_value("category", self.category)
        writer.write_bool_value("email_enabled", self.email_enabled)
        writer.write_bool_value("locked", self.locked)
    

