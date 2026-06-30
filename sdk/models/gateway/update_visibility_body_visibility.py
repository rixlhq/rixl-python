from enum import Enum

class UpdateVisibilityBody_visibility(str, Enum):
    Public = "public",
    Unlisted = "unlisted",
    Private = "private",

