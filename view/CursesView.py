import curses


class CursesView:

    def draw_borders(self, start_x, start_y, x_lenght, y_length):
        pass

    def render(self):
        self.stdscr.clear()
        #self.draw_borders(3, 3, 10, 10)
        subwin = self.stdscr.subwin(12, 12, 2, 2)
        subwin.box()
        for i in range(10):
            for j in range(10):
                self.stdscr.addstr(i+3, j+3, "▢")
        self.stdscr.refresh()
        subwin.refresh()


    def read_mouse_event(self, stdscr):
        """Считывает события мыши."""
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()
            return x, y
        return None, None

    def read_event(self, stdscr):
        return self.read_mouse_event(stdscr)
