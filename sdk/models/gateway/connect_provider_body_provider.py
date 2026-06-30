from enum import Enum

class ConnectProviderBody_provider(str, Enum):
    Google = "google",
    Apple = "apple",
    Microsoft = "microsoft",
    TgAuthResult = "tgAuthResult",

