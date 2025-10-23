import random
from typing import Dict, List, Optional, Tuple

from .enums import Orientation, ShipType, ShotStatus


class Coordinate:
    row: int
    column: int

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    @staticmethod
    def random(board_size: int):
        return Coordinate(
            row=random.randint(0, board_size-1),
            column=random.randint(0, board_size-1),
        )

    def __str__(self) -> str:
        """String representation of the Coordinate."""
        # Convert row number to letter (0 -> 'A', 1 -> 'B', etc.)
        row_char = chr(self.row + ord('A'))
        return f"{row_char}{self.column + 1}"

    def __eq__(self, other: 'Coordinate') -> bool:
        """Check equality between two Coordinate instances."""
        if not isinstance(other, Coordinate):
            return False
        return self.row == other.row and self.column == other.column

    def __hash__(self) -> int:
        """Generate a hash value for the Coordinate instance."""
        return hash((self.row, self.column))

    def is_valid(self, board_size: int) -> bool:
        """Check if the coordinate is within the bounds of the board."""
        return 0 <= self.row < board_size and 0 <= self.column < board_size
        


class Ship:
    ship_type: ShipType
    damage: int

    def __init__(self, ship_type: ShipType):
        self.ship_type = ship_type
        self.damage = 0

    @property
    def size(self) -> int:
        return self.ship_type.value

    def register_hit(self):
        self.damage += 1

    def is_sunk(self) -> bool:
        return self.damage == self.size


class Board:
    size: int
    ships: List[Ship]
    ship_map: Dict[Coordinate, Ship]
    shots_received: Dict[Coordinate, ShotStatus]

    def __init__(self, size: int):
        self.size = size
        self.ships = []
        self.ship_map = {}
        self.shots_received = {}
    
    @staticmethod
    def calculate_ship_coords(ship_size: int, start_coord: Coordinate, orientation: Orientation) -> List[Coordinate]:    
        coords = []
        for i in range(ship_size):
            if orientation == Orientation.HORIZONTAL:
                coords.append(Coordinate(start_coord.row, start_coord.column + i))
            else:
                coords.append(Coordinate(start_coord.row + i, start_coord.column))
        return coords

    def is_valid_placement(self, ship_size: int, start_coord: Coordinate, orientation: Orientation) -> bool:
        coords = Board.calculate_ship_coords(ship_size, start_coord, orientation)
        for coord in coords:
            if coord in self.ship_map or coord.is_valid(self.size) is False:
                return False
        return True

    def place_ship(self, ship: Ship, start_coord: Coordinate, orientation: Orientation):
        coords = Board.calculate_ship_coords(ship.size, start_coord, orientation)
        for coord in coords:           
            self.ship_map[coord] = ship
        self.ships.append(ship)

    def get_status_at(self, coord: Coordinate) -> ShotStatus:
        if coord in self.shots_received:
            return self.shots_received[coord]
        return ShotStatus.UNSHOT

    def get_status_grid(self) -> Dict[Coordinate, ShotStatus]:
        return self.shots_received.copy()

    def receive_shot(self, coord: Coordinate) -> Tuple[ShotStatus, Optional[str]]:
        if coord in self.ship_map:
            ship = self.ship_map[coord]
            ship.register_hit()
            self.shots_received[coord] = ShotStatus.HIT
            if ship.is_sunk():
                return ShotStatus.HIT, ship.ship_type.name
            return ShotStatus.HIT, None
        else:
            self.shots_received[coord] = ShotStatus.MISS
            return ShotStatus.MISS, None

    def all_ships_sunk(self) -> bool:
        return all(ship.is_sunk() for ship in self.ships)
