from enum import Enum

class EndpointsPostRequestBody_event_types(str, Enum):
    ImageReady = "image.ready",
    ImageFailed = "image.failed",

