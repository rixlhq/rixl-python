from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SessionStartEvent(Parsable):
    # The browser property
    browser: Optional[str] = None
    # The color_depth property
    color_depth: Optional[float] = None
    # The country property
    country: Optional[str] = None
    # The language property
    language: Optional[str] = None
    # The platform property
    platform: Optional[str] = None
    # The screen_resolution property
    screen_resolution: Optional[str] = None
    # The tg_platform property
    tg_platform: Optional[str] = None
    # The tg_version property
    tg_version: Optional[str] = None
    # The timezone property
    timezone: Optional[str] = None
    # The timezone_offset property
    timezone_offset: Optional[float] = None
    # The touch_support property
    touch_support: Optional[bool] = None
    # The user_id property
    user_id: Optional[str] = None
    # The utm_campaign property
    utm_campaign: Optional[str] = None
    # The utm_source property
    utm_source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SessionStartEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SessionStartEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SessionStartEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "color_depth": lambda n : setattr(self, 'color_depth', n.get_float_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "screen_resolution": lambda n : setattr(self, 'screen_resolution', n.get_str_value()),
            "tg_platform": lambda n : setattr(self, 'tg_platform', n.get_str_value()),
            "tg_version": lambda n : setattr(self, 'tg_version', n.get_str_value()),
            "timezone": lambda n : setattr(self, 'timezone', n.get_str_value()),
            "timezone_offset": lambda n : setattr(self, 'timezone_offset', n.get_float_value()),
            "touch_support": lambda n : setattr(self, 'touch_support', n.get_bool_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "utm_campaign": lambda n : setattr(self, 'utm_campaign', n.get_str_value()),
            "utm_source": lambda n : setattr(self, 'utm_source', n.get_str_value()),
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
        writer.write_str_value("browser", self.browser)
        writer.write_float_value("color_depth", self.color_depth)
        writer.write_str_value("country", self.country)
        writer.write_str_value("language", self.language)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("screen_resolution", self.screen_resolution)
        writer.write_str_value("tg_platform", self.tg_platform)
        writer.write_str_value("tg_version", self.tg_version)
        writer.write_str_value("timezone", self.timezone)
        writer.write_float_value("timezone_offset", self.timezone_offset)
        writer.write_bool_value("touch_support", self.touch_support)
        writer.write_str_value("user_id", self.user_id)
        writer.write_str_value("utm_campaign", self.utm_campaign)
        writer.write_str_value("utm_source", self.utm_source)
    

