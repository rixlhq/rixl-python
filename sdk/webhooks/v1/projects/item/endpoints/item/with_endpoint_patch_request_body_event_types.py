from enum import Enum

class WithEndpoint_PatchRequestBody_event_types(str, Enum):
    ImageReady = "image.ready",
    ImageFailed = "image.failed",

