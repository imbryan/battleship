from unittest import TestCase

from battleship.ai_strategy import RandomStrategy
from battleship.models import Board, ShotStatus


class RandomStrategyTestCase(TestCase):
    def setUp(self):
        self.board = Board(size=10)
        self.strategy = RandomStrategy(board_size=self.board.size)

    def test_get_next_shot(self):
        coord1 = self.strategy.get_next_shot(self.board.get_status_grid())
        self.assertTrue(coord1.is_valid())
        self.assertTrue(self.board.get_status_at(coord1) == ShotStatus.UNSHOT)
