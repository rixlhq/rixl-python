from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...common.v1.visibility import Visibility

@dataclass
class GetVideoResponse(Parsable):
    # The bitrate property
    bitrate: Optional[int] = None
    # The codec property
    codec: Optional[str] = None
    # A Duration represents a signed, fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". It is related to Timestamp in that the difference between two Timestamp values is a Duration and it can be added or subtracted from a Timestamp. Range is approximately +-10,000 years. # Examples Example 1: Compute Duration from two Timestamps in pseudo code.     Timestamp start = ...;     Timestamp end = ...;     Duration duration = ...;     duration.seconds = end.seconds - start.seconds;     duration.nanos = end.nanos - start.nanos;     if (duration.seconds < 0 && duration.nanos > 0) {       duration.seconds += 1;       duration.nanos -= 1000000000;     } else if (duration.seconds > 0 && duration.nanos < 0) {       duration.seconds -= 1;       duration.nanos += 1000000000;     } Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.     Timestamp start = ...;     Duration duration = ...;     Timestamp end = ...;     end.seconds = start.seconds + duration.seconds;     end.nanos = start.nanos + duration.nanos;     if (end.nanos < 0) {       end.seconds -= 1;       end.nanos += 1000000000;     } else if (end.nanos >= 1000000000) {       end.seconds += 1;       end.nanos -= 1000000000;     } Example 3: Compute Duration from datetime.timedelta in Python.     td = datetime.timedelta(days=3, minutes=10)     duration = Duration()     duration.FromTimedelta(td) # JSON Mapping In JSON format, the Duration type is encoded as a string rather than an object, where the string ends in the suffix "s" (indicating seconds) and is preceded by the number of seconds, with nanoseconds expressed as fractional seconds. For example, 3 seconds with 0 nanoseconds should be encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should be expressed in JSON format as "3.000000001s", and 3 seconds and 1 microsecond should be expressed in JSON format as "3.000001s".
    duration: Optional[datetime.timedelta] = None
    # The framerate property
    framerate: Optional[str] = None
    # The hdr property
    hdr: Optional[bool] = None
    # The height property
    height: Optional[int] = None
    # The id property
    id: Optional[str] = None
    # The visibility property
    visibility: Optional[Visibility] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetVideoResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetVideoResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetVideoResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...common.v1.visibility import Visibility

        from ...common.v1.visibility import Visibility

        fields: dict[str, Callable[[Any], None]] = {
            "bitrate": lambda n : setattr(self, 'bitrate', n.get_int_value()),
            "codec": lambda n : setattr(self, 'codec', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "framerate": lambda n : setattr(self, 'framerate', n.get_str_value()),
            "hdr": lambda n : setattr(self, 'hdr', n.get_bool_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(Visibility)),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_int_value("bitrate", self.bitrate)
        writer.write_str_value("codec", self.codec)
        writer.write_timedelta_value("duration", self.duration)
        writer.write_str_value("framerate", self.framerate)
        writer.write_bool_value("hdr", self.hdr)
        writer.write_int_value("height", self.height)
        writer.write_str_value("id", self.id)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_int_value("width", self.width)
    

