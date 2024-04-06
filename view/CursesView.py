import curses

class CursesView:
    """Базовый класс для представлений."""
    def __init__(self, stdscr):
        self.stdscr = stdscr
        # Включение поддержки событий мыши
        curses.mousemask(1)

    def render(self):
        pass

    def read_mouse_event(self):
        """Считывает события мыши."""
        event = self.stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()
            return x, y
        return None, None

    def read_event(self):
        pass