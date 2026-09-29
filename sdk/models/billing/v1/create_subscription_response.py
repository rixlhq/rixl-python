from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subscription_status import SubscriptionStatus

@dataclass
class CreateSubscriptionResponse(Parsable):
    # The cancel_at_period_end property
    cancel_at_period_end: Optional[bool] = None
    # The current_period_end property
    current_period_end: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The plan_id property
    plan_id: Optional[str] = None
    # The status property
    status: Optional[SubscriptionStatus] = None
    # The stripe_customer_id property
    stripe_customer_id: Optional[str] = None
    # The stripe_subscription_id property
    stripe_subscription_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateSubscriptionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateSubscriptionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateSubscriptionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .subscription_status import SubscriptionStatus

        from .subscription_status import SubscriptionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "cancel_at_period_end": lambda n : setattr(self, 'cancel_at_period_end', n.get_bool_value()),
            "current_period_end": lambda n : setattr(self, 'current_period_end', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "plan_id": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SubscriptionStatus)),
            "stripe_customer_id": lambda n : setattr(self, 'stripe_customer_id', n.get_str_value()),
            "stripe_subscription_id": lambda n : setattr(self, 'stripe_subscription_id', n.get_str_value()),
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
        writer.write_datetime_value("current_period_end", self.current_period_end)
        writer.write_str_value("id", self.id)
        writer.write_str_value("org_id", self.org_id)
        writer.write_str_value("plan_id", self.plan_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("stripe_customer_id", self.stripe_customer_id)
        writer.write_str_value("stripe_subscription_id", self.stripe_subscription_id)
    

