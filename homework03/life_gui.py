import pygame
import ui
import argparse
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def get_cell_coord(self, x: int, y: int):
        return x // self.cell_size, y // self.cell_size

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                color = "green" if self.life.curr_generation[j][i] else "white"
                a = self.cell_size
                pygame.draw.rect(self.screen, pygame.Color(color), (j * a, i * a, a, a))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        paused = False
        running = True
        while (running and self.life.is_changing and
               not self.life.is_max_generations_exceed):
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_RSHIFT:
                        paused = not paused
                if event.type == MOUSEBUTTONDOWN:
                    if paused:
                        x, y = self.get_cell_coord(* pygame.mouse.get_pos())
                        self.life.curr_generation[x][y] = abs(self.life.curr_generation[x][y] - 1)
            self.draw_grid()
            self.draw_lines()
            if not paused:
                self.life.step()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    life = GameOfLife((20, 20))
    gui = GUI(life, 10, 10)
    gui.run()
    
