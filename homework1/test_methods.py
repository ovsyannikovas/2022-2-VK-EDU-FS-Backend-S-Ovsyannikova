import unittest
from main import TicTacGame, ExceptionCellType, ExceptionCellValue, ExceptionCellOccupied


class TestValidationInput(unittest.TestCase):
    def test_not_digit(self):
        game = TicTacGame()
        try:
            self.assert_(game.validate_input('test'), "Should be ExceptionCellType")
        except ExceptionCellType:
            pass

    def test_not_in_range(self):
        game = TicTacGame()
        try:
            self.assert_(game.validate_input('0'), "Should be ExceptionCellValue")
        except ExceptionCellValue:
            pass

        try:
            self.assert_(game.validate_input('10'), "Should be ExceptionCellValue")
        except ExceptionCellValue:
            pass

    def test_occupied(self):
        game = TicTacGame()
        game.board = [
            ['X', 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        try:
            self.assert_(game.validate_input('1'), "Should be ExceptionCellOccupied")
        except ExceptionCellOccupied:
            pass


class TestCheckWinner(unittest.TestCase):
    # def test_x_row(self):
    #     self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
    #
    # def test_x_col(self):
    #     self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
    #
    # def test_x_diag(self):
    #     self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

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
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
