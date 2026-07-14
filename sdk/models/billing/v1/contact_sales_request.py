from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ContactSalesRequest(Parsable):
    # The company property
    company: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The jobTitle property
    job_title: Optional[str] = None
    # The lastName property
    last_name: Optional[str] = None
    # The message property
    message: Optional[str] = None
    # The orgId property
    org_id: Optional[str] = None
    # The phone property
    phone: Optional[str] = None
    # The website property
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContactSalesRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContactSalesRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContactSalesRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "company": lambda n : setattr(self, 'company', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "orgId": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_str_value("company", self.company)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("message", self.message)
        writer.write_str_value("orgId", self.org_id)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("website", self.website)
    

