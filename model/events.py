from dataclasses import dataclass
from enum import Enum, auto


class EventType(Enum):
    SET_FIELD = auto()
    SET_FLAG = auto()


@dataclass
class Event:
    event_type: EventType
    x: int
    y: int
