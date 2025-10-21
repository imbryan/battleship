from typing import Tuple

from .models import Board, Coordinate, Orientation, ShipType

class InvalidInputError(Exception):
    pass


def show_message(message: str):
    print(message)

def to_coord(user_input: str) -> Coordinate:
    pass

def draw_board(board: Board):
    pass

def read_board_size() -> int:
    pass

def read_coord(board_size: int) -> Coordinate:
    pass

def read_ship_placement(board_size: int, ship_type: ShipType) -> Tuple[Coordinate, Orientation]:
    pass
