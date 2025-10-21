from typing import Dict

from . import models

class AIStrategy:
    def get_next_shot(
            self, 
            board_size: int, 
            grid: Dict[models.Coordinate, models.ShotStatus]
    ) -> models.Coordinate:
        raise NotImplementedError()


class RandomStrategy(AIStrategy):
    def get_next_shot(
            self, 
            board_size: int, 
            grid: Dict[models.Coordinate, models.ShotStatus]
    ) -> models.Coordinate:
        pass
