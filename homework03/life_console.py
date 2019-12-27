import curses

from life import GameOfLife
from time import sleep
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border('|', '|', '-', '-', '+', '+', '+', '+')

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for x in range(self.life.rows):
            for y in range(self.life.cols):
                symbol = '$' if self.life.curr_generation[x][y] == 1 else ' '
                try:
                    screen.addstr(x + 1, y + 1, symbol)
                except curses.error:
                    pass

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)
        self.life.curr_generation = self.life.create_grid(True)
        running = True
        while running and self.life.is_changing and not self.life.is_max_generations_exceed:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            self.life.step()
            screen.refresh()
            sleep(0.1)
        curses.endwin()


if __name__ == '__main__':
    gui = Console(GameOfLife((20, 50), True, max_generations=300))
    gui.run()
    
