from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dashboard import Dashboard

@dataclass
class ListDashboardsResponse(Parsable):
    # The dashboards property
    dashboards: Optional[list[Dashboard]] = None
    # The page property
    page: Optional[int] = None
    # The page_size property
    page_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListDashboardsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListDashboardsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListDashboardsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dashboard import Dashboard

        from .dashboard import Dashboard

        fields: dict[str, Callable[[Any], None]] = {
            "dashboards": lambda n : setattr(self, 'dashboards', n.get_collection_of_object_values(Dashboard)),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "page_size": lambda n : setattr(self, 'page_size', n.get_int_value()),
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
        writer.write_collection_of_object_values("dashboards", self.dashboards)
        writer.write_int_value("page", self.page)
        writer.write_int_value("page_size", self.page_size)
    

