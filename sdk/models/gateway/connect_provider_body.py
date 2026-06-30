from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connect_provider_body_provider import ConnectProviderBody_provider

@dataclass
class ConnectProviderBody(AdditionalDataHolder, Parsable):
    """
    Provider token
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The provider property
    provider: Optional[ConnectProviderBody_provider] = None
    # The token property
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectProviderBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectProviderBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectProviderBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connect_provider_body_provider import ConnectProviderBody_provider

        from .connect_provider_body_provider import ConnectProviderBody_provider

        fields: dict[str, Callable[[Any], None]] = {
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(ConnectProviderBody_provider)),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_enum_value("provider", self.provider)
        writer.write_str_value("token", self.token)
        writer.write_additional_data_value(self.additional_data)
    

