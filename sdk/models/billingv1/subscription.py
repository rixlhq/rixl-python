from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Subscription(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cancel_at_period_end property
    cancel_at_period_end: Optional[bool] = None
    # The currency property
    currency: Optional[str] = None
    # The current_period_end property
    current_period_end: Optional[str] = None
    # The expiring_soon property
    expiring_soon: Optional[bool] = None
    # The id property
    id: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The plan_id property
    plan_id: Optional[str] = None
    # The plan_name property
    plan_name: Optional[str] = None
    # The plan_type property
    plan_type: Optional[str] = None
    # The price property
    price: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The trials_ending_soon property
    trials_ending_soon: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Subscription:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Subscription
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Subscription()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cancel_at_period_end": lambda n : setattr(self, 'cancel_at_period_end', n.get_bool_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "current_period_end": lambda n : setattr(self, 'current_period_end', n.get_str_value()),
            "expiring_soon": lambda n : setattr(self, 'expiring_soon', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "plan_id": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "plan_name": lambda n : setattr(self, 'plan_name', n.get_str_value()),
            "plan_type": lambda n : setattr(self, 'plan_type', n.get_str_value()),
            "price": lambda n : setattr(self, 'price', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "trials_ending_soon": lambda n : setattr(self, 'trials_ending_soon', n.get_bool_value()),
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
        writer.write_bool_value("cancel_at_period_end", self.cancel_at_period_end)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("current_period_end", self.current_period_end)
        writer.write_bool_value("expiring_soon", self.expiring_soon)
        writer.write_str_value("id", self.id)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("plan_id", self.plan_id)
        writer.write_str_value("plan_name", self.plan_name)
        writer.write_str_value("plan_type", self.plan_type)
        writer.write_str_value("price", self.price)
        writer.write_str_value("status", self.status)
        writer.write_bool_value("trials_ending_soon", self.trials_ending_soon)
        writer.write_additional_data_value(self.additional_data)
    

