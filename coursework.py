
class Chessboard:

    def __int__(self, x, y):

        self.board_height = 8
        self.board_width = 8

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
        self.placeFirstQueen = True

    def place_queen(self, x, y):
        x_coord = x - 1
        y_coord = self.board_height - y
        self.queen_placement[y_coord][x_coord] = "Q"

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
                        if self.placeFirstQueen:
                            print("\033[0m Q ", end="")
                            self.placeFirstQueen = False
                        else:
                            print("\033[0m x ", end="")
                    else:
                        print("\033[0m   ", end="")
                else:
                    if is_queen_on_tile:
                        if self.placeFirstQueen:
                            print("\033[7m Q ", end="\033[0m")
                            self.placeFirstQueen = False
                        else:
                            print("\033[7m x ", end="\033[0m")
                    else:
                        print("\033[7m   ", end="\033[0m")

                if j == 9:
                    print("   ")
            print()


if __name__ == '__main__':
    board = Chessboard.__new__(Chessboard)
    board.__int__(4, 8)
    board.place_queen(2,4)
    board.place_queen(8,3)
    board.print_chessboard()
