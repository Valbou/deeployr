from enum import Enum, IntFlag, auto


class Resources(str, Enum):
    # Users
    GROUP = "group"
    ROLE = "role"
    ROLETYPE = "roletype"


class Permissions(IntFlag):
    READ = auto()
    ACHIEVE = auto()
    UPDATE = auto()
    CREATE = auto()
    DELETE = auto()
