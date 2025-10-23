from abc import ABC, abstractmethod
from typing import Dict, Tuple

from .models import Coordinate, Ship, Board
from .enums import Orientation, ShotStatus, ShipType


class AIStrategy(ABC):
    board_size: int
    placement_tracker: Dict[Coordinate, Ship]
    shot_tracker: Dict[Coordinate, ShotStatus]

    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def get_next_placement(self, ship_type: ShipType) -> Tuple[Coordinate, Orientation]:
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

    def get_next_placement(self, ship_type: ShipType) -> Tuple[Coordinate, Orientation]:
        random_ornt = Orientation.random()
        random_coord = Coordinate.random(self.board_size)
        coords = Board.calculate_ship_coords(ship_type.value, random_coord, random_ornt)
        while any(coord in self.placement_tracker for coord in coords):
            random_ornt = Orientation.random()
            random_coord = Coordinate.random(self.board_size)
            coords = Board.calculate_ship_coords(ship_type.value, random_coord, random_ornt)
        return random_coord, random_ornt

    def get_next_shot(self) -> Coordinate:
        random_coord = Coordinate.random(self.board_size)
        while random_coord in self.shot_tracker:
            random_coord = Coordinate.random(self.board_size)
        return random_coord

    def update_shot_tracker(self, coord: Coordinate, status: ShotStatus):
        self.shot_tracker[coord] = status

    def update_placement_tracker(self, start_coord: Coordinate, ship: Ship, orientation: Orientation):
        coords = Board.calculate_ship_coords(ship.size, start_coord, orientation)
        for coord in coords:
            self.placement_tracker[coord] = ship
