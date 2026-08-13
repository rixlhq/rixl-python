from enum import Enum

class ChartFilter_operator(str, Enum):
    Eq = "eq",
    Neq = "neq",
    Gt = "gt",
    Gte = "gte",
    Lt = "lt",
    Lte = "lte",
    In_ = "in",
    Contains = "contains",

