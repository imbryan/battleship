from abc import ABC, abstractmethod
from typing import Dict

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
        pass

    def get_next_shot(
            self,
            grid: Dict[models.Coordinate, models.ShotStatus]
    ) -> models.Coordinate:
        pass
