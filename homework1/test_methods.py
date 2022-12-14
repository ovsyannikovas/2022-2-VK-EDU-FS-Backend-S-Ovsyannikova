import unittest
from main import TicTacGame, ExceptionCellType, ExceptionCellValue, ExceptionCellOccupied


class TestCheckWinner(unittest.TestCase):
    def test_o_row(self):
        game = TicTacGame()
        game.board = [
            ['O', 'O', 'O'],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assert_(game.check_winner('O'))

    def test_o_col(self):
        game = TicTacGame()
        game.board = [
            [1, 'O', 3],
            [4, 'O', 6],
            [7, 'O', 9]
        ]
        self.assert_(game.check_winner('O'))

    def test_o_diag(self):
        game = TicTacGame()
        game.board = [
            ['O', 2, 3],
            [4, 'O', 6],
            [7, 8, 'O']
        ]
        self.assert_(game.check_winner('O'))
    # обычный assert

    def test_false(self):
        game = TicTacGame()
        game.board = [
            ['O', 2, 3],
            [4, 5, 6],
            [7, 8, 'O']
        ]
        self.assertFalse(game.check_winner('O'))


class TestCheckTie(unittest.TestCase):
    def test_tie(self):
        game = TicTacGame()
        game.board = [
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']
        ]
        self.assert_(game.check_tie())

    def test_not_tie(self):
        game = TicTacGame()
        game.board = [
            ['O', 'X', 3],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']
        ]
        self.assertFalse(game.check_tie())


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


if __name__ == "__main__":
    unittest.main()
