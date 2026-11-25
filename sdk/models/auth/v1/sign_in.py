from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SignIn(Parsable):
    # auth_method is how the sign-in was started: "password", "passkey", "passkey_2fa", "totp", or "provider:<name>".
    auth_method: Optional[str] = None
    # The country property
    country: Optional[str] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    created_at: Optional[datetime.datetime] = None
    # current marks the sign-in of the access token making the request.
    current: Optional[bool] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    expires_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The ip property
    ip: Optional[str] = None
    # A point in time in RFC 3339 format, with up to nanosecond precision. Output uses UTC (`Z`); input may use an offset from UTC.
    last_used_at: Optional[datetime.datetime] = None
    # The user_agent property
    user_agent: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignIn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignIn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "auth_method": lambda n : setattr(self, 'auth_method', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "current": lambda n : setattr(self, 'current', n.get_bool_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "last_used_at": lambda n : setattr(self, 'last_used_at', n.get_datetime_value()),
            "user_agent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
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
        writer.write_str_value("auth_method", self.auth_method)
        writer.write_str_value("country", self.country)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_bool_value("current", self.current)
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("ip", self.ip)
        writer.write_datetime_value("last_used_at", self.last_used_at)
        writer.write_str_value("user_agent", self.user_agent)
    

