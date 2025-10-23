from typing import List

from .enums import Orientation
from .models import Coordinate

def calculate_ship_coords(ship_size: int, start_coord: Coordinate, orientation: Orientation) -> List[Coordinate]:    
    coords = []
    for i in range(ship_size):
        if orientation == Orientation.HORIZONTAL:
            coords.append(Coordinate(start_coord.row, start_coord.column + i))
        else:
            coords.append(Coordinate(start_coord.row + i, start_coord.column))
    return coords

