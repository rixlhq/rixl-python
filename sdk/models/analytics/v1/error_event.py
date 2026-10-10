from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ErrorEvent(Parsable):
    # The browser property
    browser: Optional[str] = None
    # The device_type property
    device_type: Optional[str] = None
    # The endpoint property
    endpoint: Optional[str] = None
    # The error_code property
    error_code: Optional[str] = None
    # The error_message property
    error_message: Optional[str] = None
    # The error_type property
    error_type: Optional[str] = None
    # The os property
    os: Optional[str] = None
    # The resource_id property
    resource_id: Optional[str] = None
    # The resource_type property
    resource_type: Optional[str] = None
    # The session_id property
    session_id: Optional[str] = None
    # The stack_trace property
    stack_trace: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ErrorEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ErrorEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ErrorEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "endpoint": lambda n : setattr(self, 'endpoint', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "error_message": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "error_type": lambda n : setattr(self, 'error_type', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "resource_type": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "session_id": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "stack_trace": lambda n : setattr(self, 'stack_trace', n.get_str_value()),
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
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("device_type", self.device_type)
        writer.write_str_value("endpoint", self.endpoint)
        writer.write_str_value("error_code", self.error_code)
        writer.write_str_value("error_message", self.error_message)
        writer.write_str_value("error_type", self.error_type)
        writer.write_str_value("os", self.os)
        writer.write_str_value("resource_id", self.resource_id)
        writer.write_str_value("resource_type", self.resource_type)
        writer.write_str_value("session_id", self.session_id)
        writer.write_str_value("stack_trace", self.stack_trace)
    

