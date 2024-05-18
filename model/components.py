from enum import Enum, auto
from typing import List
from pydantic import BaseModel, Field, validator, ValidationError
from pydantic.types import conint

from common.enums import CellDisplayStatus


class Settings(BaseModel):
    x: int = Field(gt=0, le=50)
    y: int = Field(gt=0, le=50)
    mines: int

    @validator("mines", pre=True, always=True)
    def validate_mines(cls, value, values):
        x = values.get("x")
        y = values.get("y")
        if x * y <= value:
            raise ValueError("Количество мин на поле не может превышать размер поля.")
        return value


class Cell:
    def __init__(self) -> None:
        self.hide = True  # ячейка является скрытой до тех пор, пока ее не откроют
        self.mined = False  # есть ли мина на этой ячейке
        self.flaged = False  # стоит ли флаг на этой ячейке
        self.value = 0  # значение ячейки. количество соседей с минами

    def set_mine(self) -> None:
        self.mined = True

    def set_flag(self) -> None:
        self.flaged = not self.flaged

    def open_cell(self) -> bool:
        self.hide = False

    def get_cell_display_value(self):
        if self.hide:
            return CellDisplayStatus.HIDDEN
        if self.flaged:
            return CellDisplayStatus.FLAGGED
        if self.mined:
            return CellDisplayStatus.DETONATED_MINE
        return CellDisplayStatus.OPENED_VALUE


class Board:
    def __init__(self, x, y) -> None:
        self.board = [[Cell() for _ in range(x)] for __ in range(y)]
    
    def get_board_display(self):
        displayed_board = []
        for row in self.board:
            new_row = []
            for cell in row:
                new_row.append(cell.get_cell_display_value())
            displayed_board.append(new_row)
        return displayed_board



class Game:
    def __init__(self, settings):
        self.board = Board(settings.x, settings.y)
        self.init_mines(settings.mines)

    def init_mines(self, mines_num: int):
        pass

    def get_board(self):
        return self.board


class GameService:
    difficult_settings = {
        "easy": (10, 10, 10),
        "medium": (15, 15, 20),
        "hard": (20, 20, 30),
    }

    @classmethod
    def make_settings_dict(cls, settings: tuple) -> dict:
        settings_zip = zip(("x", "y", "mines"), settings)
        return dict(settings_zip)

    @classmethod
    def get_board_params(cls, **args) -> Settings:
        difficulty = args.get("difficulty")
        if difficulty != "custom":
            settings = cls.difficult_settings[difficulty]
        else:
            settings = args.get("settings")
        return Settings(**cls.make_settings_dict(settings))

    @classmethod
    def init_game(cls, **args) -> Game:
        settings = cls.get_board_params(**args)
        return Game(settings)
