from pydantic import BaseModel, Field, validator, ValidationError
from pydantic.types import conint


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
    pass


class Board:
    def __init__(self, x, y) -> None:
        self.board = [[Cell() for _ in range(x)] for __ in range(y)]
        print(self.board)


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
    def make_settings_zip(cls, settings: tuple) -> dict:
        settings_zip = zip(("x", "y", "mines"), settings)
        return dict(settings_zip)

    @classmethod
    def get_board_params(cls, **args) -> Settings:
        difficulty = args.get("difficulty")
        if difficulty != "custom":
            settings = cls.difficult_settings[difficulty]
        else:
            settings = args.get("settings")
        return Settings(**cls.make_settings_zip(settings))

    @classmethod
    def init_game(cls, **args) -> Game:
        settings = cls.get_board_params(**args)
        return Game(settings)
