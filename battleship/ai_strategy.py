from abc import ABC, abstractmethod
from typing import Dict
import random
from . import models, enums


class AIStrategy(ABC):
    board_size: int
    shot_tracker: Dict[models.Coordinate, models.ShotStatus]

    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def get_next_shot(self) -> models.Coordinate:
        raise NotImplementedError()
    
    @abstractmethod
    def update_tracker(self, coord: models.Coordinate, status: enums.ShotStatus):
        raise NotImplementedError()


class RandomStrategy(AIStrategy):
    def __init__(self, board_size):
        self.board_size = board_size
        self.shot_tracker = {}

    def get_next_shot(self) -> models.Coordinate:
        random_coord = models.Coordinate(
            row=random.randint(0, self.board_size - 1),
            column=random.randint(0, self.board_size - 1)
        )
        while random_coord in self.shot_tracker:
            random_coord = models.Coordinate(
            row=random.randint(0, self.board_size - 1),
            column=random.randint(0, self.board_size - 1)
            )
        return random_coord

    def update_tracker(self, coord: models.Coordinate, status: enums.ShotStatus):
        pass
