import unittest
from main import TicTacGame, ExceptionCellType, ExceptionCellValue, ExceptionCellOccupied


class TestValidationInput(unittest.TestCase):
    def test_not_digit(self):
        game = TicTacGame()
        self.assertRaises(ExceptionCellType, game.validate_input, 'test')

    def test_not_in_range(self):
        game = TicTacGame()
        self.assertRaises(ExceptionCellValue, game.validate_input, '0')

    def test_occupied(self):
        game = TicTacGame()
        game.board = [
            ['X', 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertRaises(ExceptionCellOccupied, game.validate_input, '1')


class TestCheckWinner(unittest.TestCase):
    def test_o_row(self):
        game = TicTacGame()
        game.board = [
            ['O', 'O', 'O'],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(game.check_winner('O'), True, "Should be True")

    def test_o_col(self):
        game = TicTacGame()
        game.board = [
            [1, 'O', 3],
            [4, 'O', 6],
            [7, 'O', 9]
        ]
        self.assertEqual(game.check_winner('O'), True, "Should be True")

    def test_o_diag(self):
        game = TicTacGame()
        game.board = [
            ['O', 2, 3],
            [4, 'O', 6],
            [7, 8, 'O']
        ]
        self.assertEqual(game.check_winner('O'), True, "Should be True")

    def test_tie(self):
        game = TicTacGame()
        game.board = [
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']
        ]
        self.assertEqual(game.check_tie(), True, "Should be True")

    def test_not_tie(self):
        game = TicTacGame()
        game.board = [
            ['O', 'X', 3],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']
        ]
        self.assertEqual(game.check_tie(), False, "Should be False")


if __name__ == "__main__":
    unittest.main()
