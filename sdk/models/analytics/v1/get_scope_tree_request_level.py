from enum import Enum

class GetScopeTreeRequest_level(str, Enum):
    Projects = "projects",
    Resource_types = "resource_types",
    Resources = "resources",

