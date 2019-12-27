import pathlib
import random
import json

from copy import deepcopy
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(
            self,
            size: Tuple[int, int],
            randomize: bool = True,
            max_generations: Optional[float] = float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.n_generation = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        if randomize:
            return [[random.randint(0, 1) for _ in range(self.cols)] for _1 in range(self.rows)]
        else:
            return [[0 for _ in range(self.cols)] for _1 in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        Cells = []
        for x in range(cell[0] - 1, cell[0] + 2):
            for y in range(cell[1] - 1, cell[1] + 2):
                if x < 0 or y < 0 or x > self.rows - 1 or \
                        y > self.cols - 1:
                    continue
                if x == cell[0] and y == cell[1]:
                    continue
                Cells.append(self.curr_generation[x][y])
        return Cells

    def get_next_generation(self) -> Grid:
        new_grid = deepcopy(self.curr_generation)
        for x in range(self.rows):
            for y in range(self.cols):
                cell = (x, y)
                alive_neighbours = sum(self.get_neighbours(cell))
                if (alive_neighbours in (2, 3) and
                        self.curr_generation[x][y] == 1):
                    new_grid[x][y] = 1
                elif (alive_neighbours == 3 and
                      self.curr_generation[x][y] == 0):
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.n_generation += 1

    @property
    def is_max_generations_exceed(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.n_generation >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.prev_generation == self.curr_generation:
            return False
        else:
            return True

    @staticmethod
    def from_file(self, filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        file = open(self, 'a+')
        gridFromFile = file.read().split('\n')
        file.close()
        grid = []
        wight = len(gridFromFile[0])
        height = len(gridFromFile)
        for x in gridFromFile:
            Cells = []
            for symbol in x:
                Cells.append(int(symbol))
            grid.append(Cells)
        fileGame = GameOfLife((height, wight), False)
        fileGame.curr_generation = copy.deepcopy(grid)
        return fileGame

    def save(self: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        file = open(filename, 'r')
        gridDict = {}
        gridDict.update(json.loads(file.read()))
        gridDict.update({str(self.n_generation): self.curr_generation})
        file.close()
        file = open(filename, "w")
        file.write(json.dumps(gridDict))
        
