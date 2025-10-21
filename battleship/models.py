from enum import Enum
from typing import Dict, List, Optional, Tuple 


class PlayerID(Enum):
    HUMAN = 'human'
    AI = 'ai'


class Orientation(Enum):
    HORIZONTAL = 'H'
    VERTICAL = 'V'


class ShipType(Enum):
    CARRIER = 5
    BATTLESHIP = 4
    CRUISER = 3
    SUBMARINE = 3
    DESTROYER = 2


class ShotStatus(Enum):
    MISS = 'Miss'
    HIT = 'Hit'
    UNSHOT = 'Unshot'
    SHIP_SEGMENT = 'Ship_Segment'


class Coordinate:
    row: int
    column: int

    def __init__(self, row: int, column: int):
        pass

    def __str__(self) -> str:
        pass

    def __eq__(self, other: 'Coordinate') -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def is_valid(self, board_size: int) -> bool:
        pass


class Ship:
    name: ShipType
    damage: int

    def __init__(self, ship_type: ShipType):
        pass

    @property
    def size(self) -> int:
        pass

    def register_hit(self):
        pass

    def is_sunk(self) -> bool:
        pass


class Board:
    size: int
    ships: List[Ship]
    ship_map: Dict[Coordinate, Ship]
    shots_received: Dict[Coordinate, ShotStatus]

    def __init__(self, size: int):
        pass

    def is_valid_placement(self, ship_size: int, start_coord: Coordinate, orientation: Orientation) -> bool:
        pass

    def place_ship(self, ship: Ship, start_coord: Coordinate, orientation: Orientation):
        pass

    def get_status_at(self, coord: Coordinate) -> ShotStatus:
        pass

    def get_status_grid(self) -> Dict[Coordinate, ShotStatus]:
        pass

    def receive_shot(self, coord: Coordinate) -> Tuple[ShotStatus, Optional[str]]:
        pass

    def all_ships_sunk(self) -> bool:
        pass
