from enum import Enum

class ChartFilter_operator(str, Enum):
    Eq = "eq",
    Neq = "neq",
    Gt = "gt",
    Gte = "gte",
    Lt = "lt",
    Lte = "lte",
    In_ = "in",
    Not_in = "not_in",
    Contains = "contains",
    Not_contains = "not_contains",
    Starts_with = "starts_with",
    Ends_with = "ends_with",
    Between = "between",
    Is_empty = "is_empty",
    Is_not_empty = "is_not_empty",

