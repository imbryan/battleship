from abc import ABC, abstractmethod
from typing import Dict

from . import models, enums


class AIStrategy(ABC):
    board_size: int
    placement_tracker: Dict[models.Coordinate, enums.ShotStatus]
    shot_tracker: Dict[models.Coordinate, enums.ShotStatus]

    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def get_next_placement(self) -> models.Coordinate:
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
        self.placement_tracker = {}
        self.shot_tracker = {}

    def get_next_placement(self) -> models.Coordinate:
        pass

    def get_next_shot(self) -> models.Coordinate:
        random_coord = models.Coordinate.random(self.board_size)
        while random_coord in self.shot_tracker:
            random_coord = models.Coordinate.random(self.board_size)
        return random_coord

    def update_tracker(self, coord: models.Coordinate, status: enums.ShotStatus):
        pass
