from unittest import TestCase

from battleship.enums import ShipType, Orientation
from battleship.models import Coordinate
from battleship.utils import calculate_ship_coords


class CalculateShipCoordsTestCase(TestCase):
    def test_calc_coords(self):
        h_coords = calculate_ship_coords(
            ship_size=ShipType.DESTROYER.value,
            start_coord=Coordinate(0, 0),
            orientation=Orientation.HORIZONTAL,
        )
        v_coords = calculate_ship_coords(
            ship_size=ShipType.DESTROYER.value,
            start_coord=Coordinate(0, 0),
            orientation=Orientation.VERTICAL,
        )
        self.assertEqual(h_coords, [Coordinate(0, 0), Coordinate(0, 1)])
        self.assertEqual(v_coords, [Coordinate(0, 0), Coordinate(1, 0)])
