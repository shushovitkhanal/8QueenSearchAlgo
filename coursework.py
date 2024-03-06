import random


class Chessboard:

    def __int__(self, x, y):

        self.board_height = 8
        self.board_width = 8

        self.queen_coords = [0, 0, 0, 0, 0, 0, 0, 0]

        self.x_unmovable = x
        self.y_unmovable = y

        self.place_queen(x, y)
        self.placeFirstQueen = True

    def random_board(self):
        fixed_queen_x = self.x_unmovable
        fixed_queen_y = self.y_unmovable

        for i in range(0, self.board_width):
            if i == fixed_queen_x - 1:
                self.place_queen(fixed_queen_x, fixed_queen_y)
            else:
                self.place_queen(i+1, random.randint(1,8))
    def total_collisions(self):
        collisions = 0
        for i in range(0,self.board_height):
            x1 = i + 1
            y1 = self.queen_coords[i]
            for j in range(i + 1,self.board_width):
                x2 = j + 1
                y2 = self.queen_coords[j]
                if y1 != 0 and y2 != 0:
                    if not self.is_safe(x1, y1, x2, y2):
                        collisions += 1
        return collisions

    def is_safe(self, x1, y1, x2, y2):
        isSafe = False
        isOnDiagonal = False
        isOnRow = False

        if abs((y2 - y1)/(x2 - x1)) == 1:
            isOnDiagonal = True
        if y1 == y2:
            isOnRow = True

        isSafe = (not isOnRow) and (not isOnDiagonal)

        return isSafe

    def place_queen(self, x, y):
        if self.queen_coords[x - 1] == 0:
            self.queen_coords[x - 1] = y

    def remove_queen(self, x, y):

        self.queen_coords[x] = 0

    def get_queen(self, j, i):
        x_coord = j
        y_coord = self.board_height - i + 1

        is_queen_on_tile = False
        if self.queen_coords[x_coord - 1] == y_coord:
            is_queen_on_tile = True

        return is_queen_on_tile

    def print_chessboard(self):
        height = 8
        width = 8

        x_coord_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        is_cord_printed = False

        for i in range(1, height + 1):
            for j in range(1, width + 1):

                is_queen_on_tile = self.get_queen(j, i)

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
    k = 9
    l = 6

    board.__int__((k % 8 + 1), (l % 8 + 1))
    board.place_queen(8, 3)
    board.place_queen(1, 1)
    board.place_queen(7,2)
    board.print_chessboard()
    print(board.queen_coords)
    print(board.total_collisions())

    board2 = Chessboard.__new__(Chessboard)
    board2.__int__((k % 8 + 1), (l % 8 + 1))
    board2.random_board()
    board2.print_chessboard()
    print(board2.total_collisions())
