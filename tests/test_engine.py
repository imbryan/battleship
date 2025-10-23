from unittest import TestCase
from unittest.mock import Mock

from battleship.engine import BattleshipGame
from battleship.enums import PlayerID


class BattleshipGameTestCase(TestCase):
    def setUp(self):
        self.board_size = 10
        self.player1 = PlayerID.HUMAN
        self.player2 = PlayerID.AI

        self.mock_player1_board = Mock()
        self.mock_player2_board = Mock()

        self.mock_board_map = {
            self.player1: self.mock_player1_board,
            self.player2: self.mock_player2_board,
        }
        self.mock_ai_strategy = Mock()

        self.engine = BattleshipGame(
            board_size=self.board_size,
            board_map=self.mock_board_map,
            ai_strategy=self.mock_ai_strategy,
        )

    def test_initialize_placement(self):
        pass

    def test_place_ship(self):
        pass

    def test_fire_shot(self):
        pass

    def test_simulate_turn(self):
        pass

    def test_next_turn(self):
        pass

    def test_get_winner(self):
        pass
