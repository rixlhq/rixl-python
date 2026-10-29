from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .endpoints_post_request_body_event_types import EndpointsPostRequestBody_event_types

@dataclass
class EndpointsPostRequestBody(Parsable):
    # The event_types property
    event_types: Optional[list[EndpointsPostRequestBody_event_types]] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndpointsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndpointsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EndpointsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .endpoints_post_request_body_event_types import EndpointsPostRequestBody_event_types

        from .endpoints_post_request_body_event_types import EndpointsPostRequestBody_event_types

        fields: dict[str, Callable[[Any], None]] = {
            "event_types": lambda n : setattr(self, 'event_types', n.get_collection_of_enum_values(EndpointsPostRequestBody_event_types)),
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
        writer.write_collection_of_enum_values("event_types", self.event_types)
        writer.write_str_value("url", self.url)
    

