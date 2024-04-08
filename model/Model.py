from typing import List, Tuple
from custom_types import EventTypesList, SettingsType
from model.components import Game


class Model:
    """Базовый класс для моделей."""

    difficult_settings = {
        "easy": (10, 10, 10),
        "medium": (15, 15, 20),
        "hard": (20, 20, 30),
    }

    def __init__(self, **args):
        self.game = self.init_game(**args)

    def get_board_params(self, **args) -> SettingsType:
        difficulty = args.get("difficulty")
        settings = args.get("settings")

        self.difficulty = difficulty
        self.settings = settings
        if difficulty == "custom":  # проверяем кастомные параметры игры
            if (
                settings[0] * settings[1] <= settings[2]
            ):  # размер поля <= количество мин
                raise ValueError(
                    "Количество мин на поле не может превышать размер поля."
                )
            return settings
        return self.difficult_settings[difficulty]

    def init_game(self, **args) -> Game:
        x, y, mines_num = self.get_board_params(**args)
        return Game(x, y, mines_num)

    def open_cell(x: int, y: int) -> EventTypesList:
        pass

    def set_flag(x: int, y: int) -> EventTypesList:
        pass

    def get_board_status(self):
        self.game.get_board()
