from unittest import TestCase, mock, skip

from battleship import view
from battleship.enums import Orientation, ShipType
from battleship.models import Coordinate


@skip("Not implemented")
class ViewTestCase(TestCase):
    # Test read_board_size
    def test_valid_read_board_size(self):
        mock_input = ["5",]
        with mock.patch('builtins.input', side_effect=mock_input):
            result = view.read_board_size()
            self.assertTrue(5 <= result <= 26, "Board size should be at least 5x5 and uses coordinates A-Z at most")

    def test_lower_oob_read_board_size(self):
        mock_input = ["1",]
        with self.assertRaises(view.OutOfBoundsError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_board_size()
    
    def test_upper_oob_read_board_size(self):
        mock_input = ["30",]
        with self.assertRaises(view.OutOfBoundsError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_board_size()

    def test_invalid_read_board_size(self):
        mock_input = ["abc",]
        with self.assertRaises(view.InvalidInputError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_board_size()

    # Test to_coord
    def test_valid_to_coord(self):
        A1 = view.to_coord("A1")
        a1 = view.to_coord("a1")
        J10 = view.to_coord("J10")
        self.assertEqual(A1, Coordinate(0, 0))
        self.assertEqual(a1, Coordinate(0, 0))
        self.assertEqual(J10, Coordinate(9, 9))

    def test_invalid_to_coord(self):
        with self.assertRaises(view.InvalidInputError):
            view.to_coord("abc")

    def test_lower_oob_to_coord(self):
        with self.assertRaises(view.OutOfBoundsError):
            view.to_coord("A0")

    def test_upper_oob_to_coord(self):
        with self.assertRaises(view.OutOfBoundsError):
            view.to_coord("K11")
    
    # Test read_coord
    def test_valid_read_coord(self):
        mock_input = ["A1",]
        with mock.patch('builtins.input', side_effect=mock_input):
            result = view.read_coord(board_size=10)
            self.assertTrue(result.is_valid(board_size=10))
    
    def test_invalid_read_coord(self):
        mock_input = ["abc",]
        with self.assertRaises(view.InvalidInputError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_coord(board_size=10)

    def test_lower_oob_read_coord(self):
        mock_input = ["A0",]
        with self.assertRaises(view.OutOfBoundsError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_coord(board_size=10)

    def test_upper_oob_read_coord(self):
        mock_input = ["K11",]
        with self.assertRaises(view.OutOfBoundsError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_coord(board_size=10)

    # Test read_ship_type
    def test_valid_read_ship_type(self):
        mock_input = ["carrier",]
        with mock.patch('builtins.input', side_effect=mock_input):
            result = view.read_ship_type([ShipType.CARRIER,])
            self.assertEqual(result, ShipType.CARRIER)
    
    def test_invalid_read_ship_type(self):
        mock_input = ["sailboat",]
        with self.assertRaises(view.InvalidInputError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_ship_type([ShipType.CARRIER,])

    def test_oob_read_ship_type(self):
        mock_input = ["destroyer",]
        with self.assertRaises(view.OutOfBoundsError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_ship_type([ShipType.CARRIER,])

    # Test read_orientation
    def test_valid_short_read_orientation(self):
        mock_input = ["h",]
        with mock.patch('builtins.input', side_effect=mock_input):
            result = view.read_orientation()
            self.assertEqual(result, Orientation.HORIZONTAL)

    def test_valid_long_read_orientation(self):
        mock_input = ["horizontal",]
        with mock.patch('builtins.input', side_effect=mock_input):
            result = view.read_orientation()
            self.assertEqual(result, Orientation.HORIZONTAL)

    def test_invalid_read_orientation(self):
        mock_input = ["x",]
        with self.assertRaises(view.InvalidInputError):
            with mock.patch('builtins.input', side_effect=mock_input):
                view.read_orientation()
