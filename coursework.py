def is_even(number) \
        :
    if number % 2 == 0:
        return True
    else:
        return False


class Chessboard:

    def __int__(self, x, y):

        board_height = 8
        board_width = 8

        self.queen_placement = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.x_unmovable = x
        self.y_unmovable = y
        self.place_queen(x, y)

    def place_queen(self, x, y):
        x_coord = x - 1
        y_coord = y - 1
        self.queen_placement[x_coord][y_coord] = "Q"

    def remove_queen(self, x, y):
        x_coord = x - 1
        y_coord = y - 1
        self.queen_placement[x_coord][y_coord] = ''

    def get_queen(self, x, y):
        x_coord = x - 1
        y_coord = y - 1
        if self.queen_placement[x_coord][y_coord] == 'Q':
            return True
        else:
            return False

    def print_chessboard(self):
        height = 8
        width = 8

        x_coord_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        is_cord_printed = False

        for i in range(1, height + 1):
            for j in range(1, width + 1):

                is_queen_on_tile = self.get_queen(i, j)


                if not is_cord_printed:
                    print('', end='  ')
                    for item in x_coord_list:
                        print(' ' + item, end=' ')
                    print()
                    is_cord_printed = True

                if j == 1:
                    print((height + 1 - i), end=' ')

                block = (i + j) % 2
                if block == 1:
                    if is_queen_on_tile:
                        print("\033[0m \u265B ", end="")
                    else:
                        print("\033[0m   ", end="")
                else:
                    print("\033[7m   ", end="\033[0m")

                if j == 9:
                    print("   ")
            print()


'''def chess_board():
    height = 8
    width = 8

    x_coord_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    is_cord_printed = False

    for i in range(height):
        for j in range(width):

            if not is_cord_printed:
                for item in x_coord_list:
                    print(' ' + item, end=' ')
                print()
                is_cord_printed = True

            block = (i + j) % 2
            if block == 1:
                print("\033[7m   ", end="\033[0m")
            else:
                print("\033[0m   ", end='')

            if j == 8:
                print("   ")
        print()
'''

if __name__ == '__main__':
    board = Chessboard.__new__(Chessboard)
    board.__int__(4, 1)
    board.print_chessboard()
