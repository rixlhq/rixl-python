from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..protobuf.any import Any

@dataclass
class HttpBody(Parsable):
    """
    Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page. This message can be used both in streaming and non-streaming API methods in the request as well as the response. It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body. Example:     message GetResourceRequest {       // A unique request id.       string request_id = 1;       // The raw HTTP body is bound to this field.       google.api.HttpBody http_body = 2;     }     service ResourceService {       rpc GetResource(GetResourceRequest)         returns (google.api.HttpBody);       rpc UpdateResource(google.api.HttpBody)         returns (google.protobuf.Empty);     } Example with streaming methods:     service CaldavService {       rpc GetCalendar(stream google.api.HttpBody)         returns (stream google.api.HttpBody);       rpc UpdateCalendar(stream google.api.HttpBody)         returns (stream google.api.HttpBody);     } Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.
    """
    # The HTTP Content-Type header value specifying the content type of the body.
    content_type: Optional[str] = None
    # The HTTP request/response body as raw binary.
    data: Optional[bytes] = None
    # Application specific response metadata. Must be set in the first response for streaming APIs.
    extensions: Optional[list[Any]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HttpBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HttpBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HttpBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..protobuf.any import Any

        from ..protobuf.any import Any

        fields: dict[str, Callable[[Any], None]] = {
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "data": lambda n : setattr(self, 'data', n.get_bytes_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Any)),
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
        writer.write_str_value("content_type", self.content_type)
        writer.write_bytes_value("data", self.data)
        writer.write_collection_of_object_values("extensions", self.extensions)
    

