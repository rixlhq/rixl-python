from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.auth.v1.notification_category import NotificationCategory
    from .preferences_patch_request_body_user import PreferencesPatchRequestBody_user

@dataclass
class PreferencesPatchRequestBody(Parsable):
    # The category property
    category: Optional[NotificationCategory] = None
    # The email_enabled property
    email_enabled: Optional[bool] = None
    # The user property
    user: Optional[PreferencesPatchRequestBody_user] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PreferencesPatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PreferencesPatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PreferencesPatchRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.auth.v1.notification_category import NotificationCategory
        from .preferences_patch_request_body_user import PreferencesPatchRequestBody_user

        from ......models.auth.v1.notification_category import NotificationCategory
        from .preferences_patch_request_body_user import PreferencesPatchRequestBody_user

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(NotificationCategory)),
            "email_enabled": lambda n : setattr(self, 'email_enabled', n.get_bool_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(PreferencesPatchRequestBody_user)),
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
        writer.write_enum_value("category", self.category)
        writer.write_bool_value("email_enabled", self.email_enabled)
        writer.write_object_value("user", self.user)
    

