from enum import Enum

class ContentViewEvent_view_type(str, Enum):
    Start = "start",
    Watch = "watch",
    End = "end",

