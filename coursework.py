import decimal
import math
import random
import time

'''
Class Representing a Chessboard

Contains all the methods and attributes relating to the board

Program outputs using Unicode to print Chessboard in the terminal
along with performance of the algorithm

Also prints the board and performance in a txt file called example.txt
'''


class Chessboard:

    # Initializes an instance of a Chessboard
    def __int__(self):

        self.board_height = 8
        self.board_width = 8

        '''
        The index of queen_coords represents the column a queen belongs to, and
        the number within that particular index represents the row it belongs to
        '''
        self.queen_coords = [0, 0, 0, 0, 0, 0, 0, 0]

        # Last Digit of Student Number
        self.k = 9

        # Second Last Digit of Student Number
        self.l = 6

        # Coordinates of the fixed queens as described in the coursework brief
        self.x_unmovable = self.k % 8 + 1
        self.y_unmovable = self.l % 8 + 1

        self.random_board()

    '''
    Creates a board using coordinates in the format
    [row,row,row,row,row,row,row,row]
    '''

    def make_board(self, coordinates):
        # Variables for the board
        self.board_height = 8
        self.board_width = 8

        # Position of the queens
        self.queen_coords = [0, 0, 0, 0, 0, 0, 0, 0]

        # Student Number Parameters
        self.k = 9
        self.l = 6

        # Fixed Queen Position
        self.x_unmovable = self.k % 8 + 1
        self.y_unmovable = self.l % 8 + 1
        self.queen_coords = coordinates

    # Simplifies an instance of a Chessboard into Coordinates, which is easier to print
    def simplify_board(self):
        return self.queen_coords

    # Generates a random board
    def random_board(self):
        fixed_queen_x = self.x_unmovable
        fixed_queen_y = self.y_unmovable

        for i in range(0, self.board_width):
            if i == fixed_queen_x - 1:
                self.place_queen(fixed_queen_x, fixed_queen_y)
            else:
                x = i + 1
                y = random.randint(1, 8)
                self.place_queen(x, y)

    # Calculates the total number of queens which are on the same row, col or diagonals
    def total_collisions(self):
        collisions = 0
        for i in range(0, self.board_height):
            x1 = i + 1
            y1 = self.queen_coords[i]
            # For the second for loop, we are adding 1 to the ith index to avoid duplicates
            for j in range(i + 1, self.board_width):
                x2 = j + 1
                y2 = self.queen_coords[j]
                if y1 != 0 and y2 != 0:
                    if not self.is_safe(x1, y1, x2, y2):
                        collisions += 1
        return collisions

    # Checks if two pieces are on the same row,col or diagonal
    def is_safe(self, x1, y1, x2, y2):
        is_on_diagonal = False
        is_on_row = False

        # Using the slope formula to check if two queens are on same diagonal
        if abs((y2 - y1) / (x2 - x1)) == 1:
            is_on_diagonal = True
        if y1 == y2:
            is_on_row = True

        return (not is_on_row) and (not is_on_diagonal)

    # Places a queen on row x and col y
    def place_queen(self, x, y):
        # Only places a queen if there are no other queens on the same col
        if self.queen_coords[x - 1] == 0:
            self.queen_coords[x - 1] = y

    # Removes a queen from row x and col y
    def remove_queen(self, x, y):
        self.queen_coords[x] = 0

    # Checks if there is a queen present on row j and col i
    def get_queen(self, j, i):
        x_coord = j
        y_coord = self.board_height - i + 1

        is_queen_on_tile = False
        if self.queen_coords[x_coord - 1] == y_coord:
            is_queen_on_tile = True

        return is_queen_on_tile

    '''
    Prints Chessboard on the terminal using Unicode Characters in the terminal
    '''

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

                # Checking if the block is black or white
                block = (i + j) % 2
                if block == 1:
                    if is_queen_on_tile:
                        if j == self.x_unmovable:
                            print("\033[0m Q ", end="")
                            self.placeFirstQueen = False
                        else:
                            print("\033[0m x ", end="")
                    else:
                        print("\033[0m   ", end="")
                else:
                    if is_queen_on_tile:
                        if j == self.x_unmovable:
                            print("\033[7m Q ", end="\033[0m")
                            self.placeFirstQueen = False
                        else:
                            print("\033[7m x ", end="\033[0m")
                    else:
                        print("\033[7m   ", end="\033[0m")

                if j == 9:
                    print("   ")
            print()

    '''
    Prints Chessboard on the txt file
    '''

    def print_file(self, file):
        height = 8
        width = 8

        f = file
        x_coord_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H\n']
        is_cord_printed = False

        for i in range(1, height + 1):
            for j in range(1, width + 1):

                is_queen_on_tile = self.get_queen(j, i)

                if not is_cord_printed:
                    print(' ', end='', file=f)
                    for item in x_coord_list:
                        if item == 'H':
                            print(' ' + item, end='', file=f)
                        else:
                            print(' ' + item, end=' ', file=f)

                    is_cord_printed = True
                print()

                if j == 1:
                    print((height + 1 - i), end='', file=f)

                if is_queen_on_tile:
                    if j == self.x_unmovable:
                        print(" Q ", end="", file=f)
                    else:
                        print(" x ", end="", file=f)
                else:
                    print(" . ", end="", file=f)

                if j == 9:
                    print("   ", file=f)
            print(file=f)


'''
Simulated Annealing Search Algorithm
which uses different parameters to find a solution

t = Initial temperature
sch = Scheduling Used

Minimizes the total number of collisions in a chessboard until it reaches 0
'''


def sim_annealing():
    # Initial Temperature used by the algorithm
    t = 4000
    best_score = 999
    best_solution = [0, 0, 0, 0, 0, 0, 0, 0]

    # Scheduling used by the algorithm
    sch = 0.99

    solution_found = False

    start_time = time.time()
    end_time = float('inf')
    current_solution = Chessboard.__new__(Chessboard)
    current_solution.__int__()
    current_score = current_solution.total_collisions()
    current_solution = current_solution.simplify_board()

    best_solution = current_solution
    best_score = current_score

    total_iterations = 0
    while not solution_found:
        total_iterations += 1
        t *= sch
        test_solution = Chessboard.__new__(Chessboard)
        test_solution.__int__()
        test_score = test_solution.total_collisions()
        test_solution = test_solution.simplify_board()

        difference = test_score - current_score
        exp = decimal.Decimal(decimal.Decimal(math.e) ** decimal.Decimal(-difference) * decimal.Decimal(t))
        if difference <= 0 or random.uniform(0, 1) < exp:
            current_solution = test_solution
            current_score = test_score

        if current_score < best_score:
            best_solution = current_solution
            best_score = current_score

        if best_score == 0:
            solution_found = True
            end_time = time.time()

    filename = 'example.txt'
    f = open(filename, 'w')
    print(f"The best solution is {best_solution}, which has {best_score} collisions")
    print(f"The best solution is {best_solution}, which has {best_score} collisions", file=f)
    best_board = Chessboard.__new__(Chessboard)
    best_board.__init__()
    best_board.make_board(best_solution)
    best_board.print_chessboard()
    print(f"Elapsed Time: {end_time - start_time}")
    print(f"Elapsed Time: {end_time - start_time}", file=f)
    print(f"Total Iterations: {total_iterations}")
    print(f"Total Iterations: {total_iterations}", file=f)
    best_board.print_file(f)


if __name__ == '__main__':
    sim_annealing()
