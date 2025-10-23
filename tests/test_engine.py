from unittest import TestCase
from unittest.mock import Mock

from battleship.ai_strategy import AIStrategy
from battleship.engine import BattleshipGame
from battleship.enums import Orientation, PlayerID, ShipType, ShipPlacementStatus, ShotStatus
from battleship.models import Board, Coordinate, Ship


class BattleshipGameTestCase(TestCase):
    def setUp(self):
        self.board_size = 10
        self.player1 = PlayerID.HUMAN
        self.player_ai = PlayerID.AI

        self.mock_player1_board = Mock(spec=Board)
        self.mock_player_ai_board = Mock(spec=Board)

        self.mock_board_map = {
            self.player1: self.mock_player1_board,
            self.player_ai: self.mock_player_ai_board,
        }
        self.mock_ai_strategy = Mock(spec=AIStrategy)

        self.engine = BattleshipGame(
            players=(self.player1, self.player_ai),
            board_size=self.board_size,
            board_map=self.mock_board_map,
            ai_strategy=self.mock_ai_strategy,
        )

    def test_initialize_placement(self):
        self.engine.initialize_placement()
        self.assertEqual(len(self.engine.ships_to_place), 2)
        self.assertEqual(len(self.engine.ships_to_place[self.player1]), len(ShipType))

    def test_place_ship(self):
        mock_ship = Mock(spec=Ship)
        mock_ship.ship_type = ShipType.DESTROYER
        self.engine.ships_to_place = {self.player1: [mock_ship.ship_type,]}
        coord1 = Coordinate(-1, -1)
        coord2 = Coordinate.random(self.board_size)
        result1 = self.engine.place_ship(self.player1, mock_ship.ship_type, coord1, Orientation.random())
        self.engine.ships_to_place = {self.player1: [ShipType.CARRIER]}
        result2 = self.engine.place_ship(self.player1, mock_ship.ship_type, coord2, Orientation.random())
        self.assertEqual(result1, ShipPlacementStatus.INVALID, "Invalid placement due to invalid coordinates")
        self.assertEqual(result2, ShipPlacementStatus.INVALID, "Invalid placement, ship is not to be placed")

        self.engine.ships_to_place = {self.player1: [mock_ship.ship_type,]}
        result3 = self.engine.place_ship(self.player1, mock_ship.ship_type, coord2, Orientation.random())
        self.assertEqual(result3, ShipPlacementStatus.SUCCESS, "Valid placement, OK coords and ship is to be placed")

    def test_simulate_placement(self):
        self.engine.ships_to_place = {
            self.player_ai: [mem for mem in ShipType]
        }
        self.mock_ai_strategy.get_next_placement.return_value = (Coordinate.random(self.board_size), Orientation.random())
        self.mock_ai_strategy.placement_tracker = {}
        self.engine.simulate_placement()
        self.assertEqual(len(self.engine.ships_to_place[self.player_ai]), 0, "AI should have placed all ships")
        #self.assertEqual(len(self.engine.ai_strategy.placement_tracker), ShipType.total_size(), "AI should have tracked all its placements")

    def test_is_placement_complete(self):
        self.assertFalse(self.engine.is_placement_complete())

        self.engine.ships_to_place = {}
        self.assertTrue(self.engine.is_placement_complete())

        self.engine.ships_to_place = {
            self.player1: [mem for mem in ShipType]
        }
        self.assertFalse(self.engine.is_placement_complete())

    def test_fire_shot(self):
        coord1 = Coordinate(-1, -1)
        coord2 = Coordinate(0, 0)
        coord3 = Coordinate(1, 1)
        result1 = self.engine.fire_shot(self.player1, coord1)
        self.assertEqual(result1[0], ShotStatus.INVALID)

        self.mock_player_ai_board.shots_received = {
            coord2: ShotStatus.HIT,
        }
        result2 = self.engine.fire_shot(self.player1, coord2)
        self.assertEqual(result2[0], ShotStatus.ALREADY_SHOT)

        result3 = self.engine.fire_shot(self.player1, coord3)
        self.assertEqual(result3[0], ShotStatus.MISS)

    def test_simulate_turn(self):
        pass

    def test_next_turn(self):
        self.engine.current_player = self.player_ai
        self.engine.next_turn()
        self.assertEqual(self.engine.current_player, self.player1)

    def test_get_winner(self):
        self.mock_player_ai_board.ships = [Ship(ship_type) for ship_type in ShipType]
        for ship in self.mock_player_ai_board.ships:
            ship.damage = ship.ship_type.value
        self.assertEqual(self.engine.get_winner(), self.player1)
