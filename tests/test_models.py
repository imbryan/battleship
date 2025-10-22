from unittest import TestCase

from battleship.models import Board, Coordinate, Orientation, Ship, ShipType, ShotStatus

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


class ShipTestCase(TestCase):
    def test_size(self):
        carrier = Ship(ShipType.CARRIER)
        self.assertEqual(carrier.size, ShipType.CARRIER.value)
    
    def test_sinking(self):
        destroyer = Ship(ShipType.DESTROYER)
        for _ in range(ShipType.DESTROYER.value):
            destroyer.register_hit()
        self.assertTrue(destroyer.is_sunk())

        carrier = Ship(ShipType.CARRIER)
        self.assertFalse(carrier.is_sunk())


class BoardTestCase(TestCase):
    def setUp(self):
        self.board = Board(size=10)

    def test_valid_placement(self):
        coord1 = Coordinate(0, 0)
        coord2 = Coordinate(9, 9)
        self.assertTrue(self.board.is_valid_placement(
            ship_size=ShipType.DESTROYER.value,
            start_coord=coord1,
            orientation=Orientation.HORIZONTAL,
        ))
        self.assertFalse(self.board.is_valid_placement(
            ship_size=ShipType.DESTROYER.value,
            start_coord=coord2,
            orientation=Orientation.HORIZONTAL,
        ), "Placement should be invalid due to overflow.")

        destroyer = Ship(ShipType.DESTROYER)
        for i in range(ShipType.DESTROYER.value):
            self.board.ship_map[Coordinate(i, 0)] = destroyer
        
        self.assertFalse(self.board.is_valid_placement(
            ship_size=ShipType.CARRIER.value,
            start_coord=coord1,
            orientation=Orientation.HORIZONTAL
        ), "Placement should be invalid due to overlap.")

    def test_place_ship(self):
        destroyer = Ship(ShipType.DESTROYER)
        self.board.place_ship(destroyer, Coordinate(0, 0), Orientation.HORIZONTAL)
        self.assertIn(destroyer, self.board.ships)
        self.assertIn(destroyer, self.board.ship_map.values())
        self.assertEqual(len(self.board.ship_map.keys()), ShipType.DESTROYER.value)

    def test_get_status_at(self):
        self.board.shots_received[Coordinate(0, 0)] = ShotStatus.UNSHOT
        self.board.shots_received[Coordinate(4, 4)] = ShotStatus.HIT
        self.board.shots_received[Coordinate(9, 9)] = ShotStatus.MISS
        self.assertEqual(self.board.get_status_at(Coordinate(0, 0)), ShotStatus.UNSHOT)
        self.assertEqual(self.board.get_status_at(Coordinate(4, 4)), ShotStatus.HIT)
        self.assertEqual(self.board.get_status_at(Coordinate(9, 9)), ShotStatus.MISS)

    def test_get_status_grid(self):
        self.assertEqual(self.board.get_status_grid(), {}, "Status grid should be empty.")
        self.board.shots_received[Coordinate(0, 0)] = ShotStatus.UNSHOT
        self.assertEqual(self.board.get_status_grid(), { Coordinate(0, 0): ShotStatus.UNSHOT })

    def test_receive_shot(self):
        destroyer = Ship(ShipType.DESTROYER)
        for i in range(ShipType.DESTROYER.value):
            self.board.ship_map[Coordinate(i, 0)] = destroyer
        self.assertEqual(self.board.receive_shot(Coordinate(0, 1)), (ShotStatus.MISS, None))
        self.assertEqual(self.board.receive_shot(Coordinate(0, 0)), (ShotStatus.HIT, None))
        self.assertEqual(self.board.receive_shot(Coordinate(1, 0)), (ShotStatus.HIT, 'DESTROYER'), "Should have sunk the destroyer.")

    def test_all_ships_sunk(self):
        destroyer = Ship(ShipType.DESTROYER)
        self.board.ships = [destroyer,]
        self.assertFalse(self.board.all_ships_sunk())
        destroyer.damage = 2
        self.assertTrue(self.board.all_ships_sunk())
