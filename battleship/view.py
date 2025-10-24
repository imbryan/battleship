from typing import List, Tuple, Optional

from .models import Board, Coordinate, Orientation, ShipType

class InvalidInputError(Exception):
    def __init__(self, message="Invalid input provided."):
        super().__init__(message)
        self.message = message


class OutOfBoundsError(InvalidInputError):
    def __init__(self, message="Input is out of bounds."):
        super().__init__(message)
        self.message = message


def show_message(message: str, end: Optional[str]):
    print(message, end=end)

def confirm(message: str) -> bool:
    user_input = input(f"{message} Y/n: ")
    return user_input.lower() == "y"

def to_coord(user_input: str) -> Coordinate:
    # If not in "A1" format, raise InvalidInputError
    # If Coordinate is valid is false, raise OutOfBoundsError
    pass

def draw_board(board: Board):
    pass

def read_board_size() -> int:
    pass

def read_coord(board_size: int) -> Coordinate:
    # Read user input
    # Call to_coord
    pass

def read_ship_type(ship_types: List[ShipType]) -> ShipType:
    pass

def read_orientation() -> Orientation:
    pass
