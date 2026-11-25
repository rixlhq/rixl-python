from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_post_request_body_user import DomainPostRequestBody_user

@dataclass
class DomainPostRequestBody(Parsable):
    # The domain property
    domain: Optional[str] = None
    # The user property
    user: Optional[DomainPostRequestBody_user] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .domain_post_request_body_user import DomainPostRequestBody_user

        from .domain_post_request_body_user import DomainPostRequestBody_user

        fields: dict[str, Callable[[Any], None]] = {
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(DomainPostRequestBody_user)),
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
        writer.write_str_value("domain", self.domain)
        writer.write_object_value("user", self.user)
    

