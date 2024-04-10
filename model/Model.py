from typing import List, Tuple
from custom_types import EventTypesList
from model.components import GameService


class Model:
    """Базовый класс для моделей."""

    def __init__(self, **args):
        self.game = GameService.init_game(**args)

    def open_cell(x: int, y: int) -> EventTypesList:
        pass

    def set_flag(x: int, y: int) -> EventTypesList:
        pass

    def get_board_status(self):
        self.game.get_board()
