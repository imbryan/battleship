from abc import ABC, abstractmethod
from typing import Dict
import random
from . import models

class AIStrategy(ABC):
    board_size: int

    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def get_next_shot(
            self, 
            board_size: int, 
            grid: Dict[models.Coordinate, models.ShotStatus]
    ) -> models.Coordinate:
        raise NotImplementedError()


class RandomStrategy(AIStrategy):
    def __init__(self, board_size):
        self.board_size = board_size

    def get_next_shot(self, grid: Dict[models.Coordinate, models.ShotStatus]) -> models.Coordinate:
        random_coord = models.Coordinate(
            row=random.randint(0, self.board_size - 1),
            column=random.randint(0, self.board_size - 1)
        )
        while random_coord in grid:
            random_coord = models.Coordinate(
            row=random.randint(0, self.board_size - 1),
            column=random.randint(0, self.board_size - 1)
            )
        return random_coord