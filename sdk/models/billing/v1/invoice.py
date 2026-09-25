from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .invoice_status import InvoiceStatus

@dataclass
class Invoice(Parsable):
    # The amount property
    amount: Optional[str] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The currency property
    currency: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The due_date property
    due_date: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The org_id property
    org_id: Optional[str] = None
    # The paid_at property
    paid_at: Optional[datetime.datetime] = None
    # The status property
    status: Optional[InvoiceStatus] = None
    # The subscription_id property
    subscription_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Invoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Invoice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Invoice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .invoice_status import InvoiceStatus

        from .invoice_status import InvoiceStatus

        fields: dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "due_date": lambda n : setattr(self, 'due_date', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "paid_at": lambda n : setattr(self, 'paid_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(InvoiceStatus)),
            "subscription_id": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
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
        writer.write_str_value("amount", self.amount)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("due_date", self.due_date)
        writer.write_str_value("id", self.id)
        writer.write_str_value("org_id", self.org_id)
        writer.write_datetime_value("paid_at", self.paid_at)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subscription_id", self.subscription_id)
    

