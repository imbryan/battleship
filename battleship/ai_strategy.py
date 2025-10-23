from abc import ABC, abstractmethod
from typing import Dict, Tuple

from .models import Coordinate, Ship
from .enums import Orientation, ShotStatus


class AIStrategy(ABC):
    board_size: int
    placement_tracker: Dict[Coordinate, Ship]
    shot_tracker: Dict[Coordinate, ShotStatus]

    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def get_next_placement(self) -> Tuple[Coordinate, Orientation]:
        raise NotImplementedError()
        
    @abstractmethod
    def get_next_shot(self) -> Coordinate:
        raise NotImplementedError()
    
    @abstractmethod
    def update_placement_tracker(self, coord: Coordinate, status: ShotStatus):
        raise NotImplementedError()

    @abstractmethod
    def update_shot_tracker(self, start_coord: Coordinate, ship: Ship, orientation: Orientation):
        raise NotImplementedError()


class RandomStrategy(AIStrategy):
    def __init__(self, board_size):
        self.board_size = board_size
        self.placement_tracker = {}
        self.shot_tracker = {}

    def get_next_placement(self) -> Tuple[Coordinate, Orientation]:
        random_coord = Coordinate.random(self.board_size)
        while random_coord in self.placement_tracker:
            random_coord = Coordinate.random(self.board_size)
        return random_coord, Orientation.random()

    def get_next_shot(self) -> Coordinate:
        random_coord = Coordinate.random(self.board_size)
        while random_coord in self.shot_tracker:
            random_coord = Coordinate.random(self.board_size)
        return random_coord

    def update_shot_tracker(self, coord: Coordinate, status: ShotStatus):
        self.shot_tracker[coord] = status

    def update_placement_tracker(self, start_coord: Coordinate, ship: Ship, orientation: Orientation):
        for i in range(ship.size):
            if orientation == Orientation.HORIZONTAL:
                coord = Coordinate(start_coord.row, start_coord.column + i)
                self.placement_tracker[coord] = ship
            else:  # VERTICAL
                coord = Coordinate(start_coord.row + i, start_coord.column)
                self.placement_tracker[coord] = ship
