from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .plan_type import PlanType

@dataclass
class Plan(Parsable):
    # The currency property
    currency: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The interval property
    interval: Optional[str] = None
    # The interval_count property
    interval_count: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The plan_type property
    plan_type: Optional[PlanType] = None
    # The price property
    price: Optional[str] = None
    # The sort_order property
    sort_order: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Plan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Plan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Plan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .plan_type import PlanType

        from .plan_type import PlanType

        fields: dict[str, Callable[[Any], None]] = {
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "interval": lambda n : setattr(self, 'interval', n.get_str_value()),
            "interval_count": lambda n : setattr(self, 'interval_count', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "plan_type": lambda n : setattr(self, 'plan_type', n.get_enum_value(PlanType)),
            "price": lambda n : setattr(self, 'price', n.get_str_value()),
            "sort_order": lambda n : setattr(self, 'sort_order', n.get_int_value()),
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
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_str_value("interval", self.interval)
        writer.write_int_value("interval_count", self.interval_count)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("plan_type", self.plan_type)
        writer.write_str_value("price", self.price)
        writer.write_int_value("sort_order", self.sort_order)
    

