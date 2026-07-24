from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StorageUsage(Parsable):
    # The image_file_count property
    image_file_count: Optional[int] = None
    # A Timestamp represents a point in time independent of any time zone or local calendar, encoded as a count of seconds and fractions of seconds at nanosecond resolution. The count is relative to an epoch at UTC midnight on January 1, 1970, in the proleptic Gregorian calendar which extends the Gregorian calendar backwards to year one. All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap second table is needed for interpretation, using a [24-hour linear smear](https://developers.google.com/time/smear). The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) date strings. # Examples Example 1: Compute Timestamp from POSIX `time()`.     Timestamp timestamp;     timestamp.set_seconds(time(NULL));     timestamp.set_nanos(0); Example 2: Compute Timestamp from POSIX `gettimeofday()`.     struct timeval tv;     gettimeofday(&tv, NULL);     Timestamp timestamp;     timestamp.set_seconds(tv.tv_sec);     timestamp.set_nanos(tv.tv_usec * 1000); Example 3: Compute Timestamp from Win32 `GetSystemTimeAsFileTime()`.     FILETIME ft;     GetSystemTimeAsFileTime(&ft);     UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;     // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z     // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.     Timestamp timestamp;     timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));     timestamp.set_nanos((INT32) ((ticks % 10000000) * 100)); Example 4: Compute Timestamp from Java `System.currentTimeMillis()`.     long millis = System.currentTimeMillis();     Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)         .setNanos((int) ((millis % 1000) * 1000000)).build(); Example 5: Compute Timestamp from Java `Instant.now()`.     Instant now = Instant.now();     Timestamp timestamp =         Timestamp.newBuilder().setSeconds(now.getEpochSecond())             .setNanos(now.getNano()).build(); Example 6: Compute Timestamp from current time in Python.     timestamp = Timestamp()     timestamp.GetCurrentTime() # JSON Mapping In JSON format, the Timestamp type is encoded as a string in the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where {year} is always expressed using four digits while {month}, {day}, {hour}, {min}, and {sec} are zero-padded to two digits each. The fractional seconds, which can go up to 9 digits (i.e. up to 1 nanosecond resolution), are optional. The "Z" suffix indicates the timezone ("UTC"); the timezone is required. A proto3 JSON serializer should always use UTC (as indicated by "Z") when printing the Timestamp type and a proto3 JSON parser should be able to accept both UTC and other timezones (as indicated by an offset). For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30 UTC on January 15, 2017. In JavaScript, one can convert a Date object to this format using the standard [toISOString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString) method. In Python, a standard `datetime.datetime` object can be converted to this format using [`strftime`](https://docs.python.org/2/library/time.html#time.strftime) with the time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java, one can use the Joda Time's [`ISODateTimeFormat.dateTime()`]( http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime() ) to obtain a formatter capable of generating timestamps in this format.
    last_updated: Optional[datetime.datetime] = None
    # The max_image_count property
    max_image_count: Optional[int] = None
    # The max_project_count property
    max_project_count: Optional[int] = None
    # The max_video_count property
    max_video_count: Optional[int] = None
    # The org_id property
    org_id: Optional[str] = None
    # The project_count property
    project_count: Optional[int] = None
    # A Timestamp represents a point in time independent of any time zone or local calendar, encoded as a count of seconds and fractions of seconds at nanosecond resolution. The count is relative to an epoch at UTC midnight on January 1, 1970, in the proleptic Gregorian calendar which extends the Gregorian calendar backwards to year one. All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap second table is needed for interpretation, using a [24-hour linear smear](https://developers.google.com/time/smear). The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) date strings. # Examples Example 1: Compute Timestamp from POSIX `time()`.     Timestamp timestamp;     timestamp.set_seconds(time(NULL));     timestamp.set_nanos(0); Example 2: Compute Timestamp from POSIX `gettimeofday()`.     struct timeval tv;     gettimeofday(&tv, NULL);     Timestamp timestamp;     timestamp.set_seconds(tv.tv_sec);     timestamp.set_nanos(tv.tv_usec * 1000); Example 3: Compute Timestamp from Win32 `GetSystemTimeAsFileTime()`.     FILETIME ft;     GetSystemTimeAsFileTime(&ft);     UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;     // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z     // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.     Timestamp timestamp;     timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));     timestamp.set_nanos((INT32) ((ticks % 10000000) * 100)); Example 4: Compute Timestamp from Java `System.currentTimeMillis()`.     long millis = System.currentTimeMillis();     Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)         .setNanos((int) ((millis % 1000) * 1000000)).build(); Example 5: Compute Timestamp from Java `Instant.now()`.     Instant now = Instant.now();     Timestamp timestamp =         Timestamp.newBuilder().setSeconds(now.getEpochSecond())             .setNanos(now.getNano()).build(); Example 6: Compute Timestamp from current time in Python.     timestamp = Timestamp()     timestamp.GetCurrentTime() # JSON Mapping In JSON format, the Timestamp type is encoded as a string in the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where {year} is always expressed using four digits while {month}, {day}, {hour}, {min}, and {sec} are zero-padded to two digits each. The fractional seconds, which can go up to 9 digits (i.e. up to 1 nanosecond resolution), are optional. The "Z" suffix indicates the timezone ("UTC"); the timezone is required. A proto3 JSON serializer should always use UTC (as indicated by "Z") when printing the Timestamp type and a proto3 JSON parser should be able to accept both UTC and other timezones (as indicated by an offset). For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30 UTC on January 15, 2017. In JavaScript, one can convert a Date object to this format using the standard [toISOString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString) method. In Python, a standard `datetime.datetime` object can be converted to this format using [`strftime`](https://docs.python.org/2/library/time.html#time.strftime) with the time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java, one can use the Joda Time's [`ISODateTimeFormat.dateTime()`]( http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime() ) to obtain a formatter capable of generating timestamps in this format.
    snapshot_date: Optional[datetime.datetime] = None
    # The total_file_count property
    total_file_count: Optional[int] = None
    # The total_video_minutes property
    total_video_minutes: Optional[str] = None
    # The video_file_count property
    video_file_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StorageUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "image_file_count": lambda n : setattr(self, 'image_file_count', n.get_int_value()),
            "last_updated": lambda n : setattr(self, 'last_updated', n.get_datetime_value()),
            "max_image_count": lambda n : setattr(self, 'max_image_count', n.get_int_value()),
            "max_project_count": lambda n : setattr(self, 'max_project_count', n.get_int_value()),
            "max_video_count": lambda n : setattr(self, 'max_video_count', n.get_int_value()),
            "org_id": lambda n : setattr(self, 'org_id', n.get_str_value()),
            "project_count": lambda n : setattr(self, 'project_count', n.get_int_value()),
            "snapshot_date": lambda n : setattr(self, 'snapshot_date', n.get_datetime_value()),
            "total_file_count": lambda n : setattr(self, 'total_file_count', n.get_int_value()),
            "total_video_minutes": lambda n : setattr(self, 'total_video_minutes', n.get_str_value()),
            "video_file_count": lambda n : setattr(self, 'video_file_count', n.get_int_value()),
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
        writer.write_int_value("image_file_count", self.image_file_count)
        writer.write_datetime_value("last_updated", self.last_updated)
        writer.write_int_value("max_image_count", self.max_image_count)
        writer.write_int_value("max_project_count", self.max_project_count)
        writer.write_int_value("max_video_count", self.max_video_count)
        writer.write_str_value("org_id", self.org_id)
        writer.write_int_value("project_count", self.project_count)
        writer.write_datetime_value("snapshot_date", self.snapshot_date)
        writer.write_int_value("total_file_count", self.total_file_count)
        writer.write_str_value("total_video_minutes", self.total_video_minutes)
        writer.write_int_value("video_file_count", self.video_file_count)
    

