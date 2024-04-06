import curses

from controller.BaseController import BaseController


class MouseController(BaseController):
    def handle_input(self, input_key):
        if input_key == 'q':
            return  # Выход из приложения
        # Дополнительная логика для обработки других вводов

    def main_loop(self):
        curses.wrapper(self.run)

    def run(self, stdscr):
        self.view.stdscr = stdscr
        while True:
            x, y = self.view.read_event()
            if x is not None and y is not None:
                self.handle_mouse_click(x, y)
            key = stdscr.getkey()
            if key == 'q':
                break
            self.handle_input(key)

    def handle_mouse_click(self, x, y):
        print(f"Клик мыши в позиции: {x}, {y}")