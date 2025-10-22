from unittest import TestCase

from battleship.models import Coordinate, Ship, ShipType

class CoordinateTestCase(TestCase):
    def test_str(self):
        coord1 = Coordinate(0, 0)
        coord2 = Coordinate(9, 9)
        coord3 = Coordinate(10, 10)
        self.assertEqual(coord1.__str__(), "A1")
        self.assertEqual(coord2.__str__(), "J10")
        self.assertEqual(coord3.__str__(), "K11")

    def test_eq(self):
        coord1 = Coordinate(0, 0)
        coord2 = Coordinate(9, 9)
        coord3 = None
        self.assertTrue(coord1 == coord1)
        self.assertFalse(coord1 == coord2)
        self.assertFalse(coord1 == coord3)

    def test_hash(self):
        coord1 = Coordinate(0, 0)
        coord2 = Coordinate(0, 0)
        self.assertTrue(coord1.__hash__() == coord2.__hash__())

    def test_is_valid(self):
        coord1 = Coordinate(0, 0)
        coord2 = Coordinate(10, 10)
        board_size1 = 10
        self.assertTrue(coord1.is_valid(board_size1))
        self.assertFalse(coord2.is_valid(board_size1))
