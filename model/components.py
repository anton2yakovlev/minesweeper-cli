class Cell:
    pass


class Board:
    def __init__(self, x, y) -> None:
        self.board = [[Cell() for _ in range(x)] for __ in range(y)]
        print(self.board)


class Game:
    def __init__(self, x, y, mines_num):
        self.board = Board(x, y)
        self.init_mines(mines_num)

    def init_mines(self, mines_num: int):
        pass

    def get_board(self):
        return self.board
