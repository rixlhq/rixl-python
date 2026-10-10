from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subscription_status import SubscriptionStatus

@dataclass
class SubscriptionHistoryItem(Parsable):
    # The cancel_at_period_end property
    cancel_at_period_end: Optional[bool] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The currency property
    currency: Optional[str] = None
    # The current_period_end property
    current_period_end: Optional[datetime.datetime] = None
    # The end_date property
    end_date: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The plan_id property
    plan_id: Optional[str] = None
    # The plan_name property
    plan_name: Optional[str] = None
    # The price property
    price: Optional[str] = None
    # The start_date property
    start_date: Optional[datetime.datetime] = None
    # The status property
    status: Optional[SubscriptionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubscriptionHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubscriptionHistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubscriptionHistoryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .subscription_status import SubscriptionStatus

        from .subscription_status import SubscriptionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "cancel_at_period_end": lambda n : setattr(self, 'cancel_at_period_end', n.get_bool_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "current_period_end": lambda n : setattr(self, 'current_period_end', n.get_datetime_value()),
            "end_date": lambda n : setattr(self, 'end_date', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "plan_id": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "plan_name": lambda n : setattr(self, 'plan_name', n.get_str_value()),
            "price": lambda n : setattr(self, 'price', n.get_str_value()),
            "start_date": lambda n : setattr(self, 'start_date', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SubscriptionStatus)),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("currency", self.currency)
        writer.write_datetime_value("current_period_end", self.current_period_end)
        writer.write_datetime_value("end_date", self.end_date)
        writer.write_str_value("id", self.id)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("plan_id", self.plan_id)
        writer.write_str_value("plan_name", self.plan_name)
        writer.write_str_value("price", self.price)
        writer.write_datetime_value("start_date", self.start_date)
        writer.write_enum_value("status", self.status)
    

