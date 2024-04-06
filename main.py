from view import CursesView
from model import Model
from controller import CursesMouseController


if __name__ == "__main__":
    model = Model()
    view = CursesView()
    controller = CursesMouseController(model, view)
    controller.main_loop()
