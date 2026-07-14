from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UserInfo(Parsable):
    # The activeOrgId property
    active_org_id: Optional[str] = None
    # The countryCode property
    country_code: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The emailVerified property
    email_verified: Optional[bool] = None
    # The firstName property
    first_name: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The imageUrl property
    image_url: Optional[str] = None
    # The languageCode property
    language_code: Optional[str] = None
    # The lastName property
    last_name: Optional[str] = None
    # The username property
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activeOrgId": lambda n : setattr(self, 'active_org_id', n.get_str_value()),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "emailVerified": lambda n : setattr(self, 'email_verified', n.get_bool_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "imageUrl": lambda n : setattr(self, 'image_url', n.get_str_value()),
            "languageCode": lambda n : setattr(self, 'language_code', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
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
        writer.write_str_value("activeOrgId", self.active_org_id)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("email", self.email)
        writer.write_bool_value("emailVerified", self.email_verified)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("imageUrl", self.image_url)
        writer.write_str_value("languageCode", self.language_code)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("username", self.username)
    

