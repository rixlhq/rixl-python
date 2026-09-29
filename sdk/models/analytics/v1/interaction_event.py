from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InteractionEvent(Parsable):
    # The browser property
    browser: Optional[str] = None
    # The click_x property
    click_x: Optional[int] = None
    # The click_y property
    click_y: Optional[int] = None
    # The device_type property
    device_type: Optional[str] = None
    # The element_id property
    element_id: Optional[str] = None
    # The element_type property
    element_type: Optional[str] = None
    # The interaction_type property
    interaction_type: Optional[str] = None
    # The page property
    page: Optional[str] = None
    # The page_url property
    page_url: Optional[str] = None
    # The scroll_depth property
    scroll_depth: Optional[float] = None
    # The search_query property
    search_query: Optional[str] = None
    # The session_id property
    session_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InteractionEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InteractionEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InteractionEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "click_x": lambda n : setattr(self, 'click_x', n.get_int_value()),
            "click_y": lambda n : setattr(self, 'click_y', n.get_int_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "element_id": lambda n : setattr(self, 'element_id', n.get_str_value()),
            "element_type": lambda n : setattr(self, 'element_type', n.get_str_value()),
            "interaction_type": lambda n : setattr(self, 'interaction_type', n.get_str_value()),
            "page": lambda n : setattr(self, 'page', n.get_str_value()),
            "page_url": lambda n : setattr(self, 'page_url', n.get_str_value()),
            "scroll_depth": lambda n : setattr(self, 'scroll_depth', n.get_float_value()),
            "search_query": lambda n : setattr(self, 'search_query', n.get_str_value()),
            "session_id": lambda n : setattr(self, 'session_id', n.get_str_value()),
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
        writer.write_int_value("click_x", self.click_x)
        writer.write_int_value("click_y", self.click_y)
        writer.write_str_value("device_type", self.device_type)
        writer.write_str_value("element_id", self.element_id)
        writer.write_str_value("element_type", self.element_type)
        writer.write_str_value("interaction_type", self.interaction_type)
        writer.write_str_value("page", self.page)
        writer.write_str_value("page_url", self.page_url)
        writer.write_float_value("scroll_depth", self.scroll_depth)
        writer.write_str_value("search_query", self.search_query)
        writer.write_str_value("session_id", self.session_id)
    

