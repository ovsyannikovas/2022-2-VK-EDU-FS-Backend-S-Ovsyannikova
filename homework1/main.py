import os
from time import sleep


class ExceptionCellType(Exception):
    """
    Пользовательское исключение: ошибка типа "Значение клетки не является целым числом!"
    """


class ExceptionCellValue(Exception):
    """
    Пользовательское исключение: ошибка типа "Значение клетки не является целым числом!"
    """


class ExceptionCellOccupied(Exception):
    """
    Пользовательское исключение: ошибка типа "Клетка занята!"
    """


class TicTacGame:
    """
    Класс игры крестики-нолики.
    """
    cell_coords_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0),
                        5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}

    def __init__(self):
        self.board = [list(range(3 * i + 1, 3 * (i + 1) + 1)) for i in range(3)]
        self.player = 0

    def show_board(self):
        """
        Выводит поле игры в виде таблицы 3х3.
        """
        os.system('cls')
        table = '\n' + '\n\t---+---+---\n'.join(
            ['\t ' + ' | '.join(map(str, self.board[i])) for i in range(3)])
        print('\n\tИгра крестики - нолики\n', table)

    def validate_input(self, cell):
        """
        Валидация введенного пользователем значения клетки.
        :param cell: Значение клетки
        """
        # if not digit
        if not cell.isdigit():
            raise ExceptionCellType

        # if not in range
        if not 1 <= int(cell) <= 9:
            raise ExceptionCellValue

        # if the cell is occupied
        if self.board[self.cell_coords_dict[int(cell)][0]][self.cell_coords_dict[int(cell)][1]] != int(cell):
            raise ExceptionCellOccupied

    def start_game(self):
        """
        Главный цикл игры.
        """
        while True:
            sign = 'X' if self.player == 0 else 'O'
            self.show_board()
            cell = input(f'\n\tВыберите клетку, чтобы поставить "{sign}": ')

            try:
                self.validate_input(cell)
            except ExceptionCellType:
                print('\n\tЗначение клетки не является целым числом!')
                sleep(2)
                continue
            except ExceptionCellValue:
                print('\n\tЗначение клетки выходит за пределы допустимых значений!')
                sleep(2)
                continue
            except ExceptionCellOccupied:
                print('\n\tКлетка занята!')
                sleep(2)
                continue

            self.board[self.cell_coords_dict[int(cell)][0]][self.cell_coords_dict[int(cell)][1]] = sign

            win = self.check_winner(sign)
            if win or self.check_tie():
                self.show_board()

                if win:
                    print(f'\n\tПобедитель "{sign}"!')
                else:
                    print('\n\tНичья!')

                tmp = input('').split(" ")[0]
                print(tmp)
                break

            self.player = (self.player + 1) % 2

    def check_tie(self) -> bool:
        """
        Проверка ничьей.
        :return: Булевое значение, есть ли ничья
        """
        empty_cells = 0
        for row in self.board:
            empty_cells += len(list(filter(lambda x: isinstance(x, int), row)))
        return empty_cells == 0

    def check_winner(self, sign) -> bool:
        """
        Проверка выигрыша знака sign.
        :param sign: Знак для проверки выигрыша
        :return: Булевое значение, выиграл ли знак
        """
        brd = self.board

        # check rows
        for i in range(3):
            if brd[i][0] == brd[i][1] == brd[i][2] == sign:
                return True

        # check cols
        for j in range(3):
            if brd[0][j] == brd[1][j] == brd[2][j] == sign:
                return True

        # check diags
        if brd[0][0] == brd[1][1] == brd[2][2] == sign or \
                brd[0][2] == brd[1][1] == brd[2][0] == sign:
            return True


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
