from enum import Enum

class ContentViewEvent_page(str, Enum):
    Profile = "profile",
    Feed = "feed",
    Standalone = "standalone",

