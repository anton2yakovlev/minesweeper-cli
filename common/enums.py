from enum import Enum, auto


class CellDisplayStatus(Enum):
    HIDDEN = auto()
    FLAGGED = auto()
    OPENED_VALUE = auto()
    DETONATED_MINE = auto()
