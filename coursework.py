def is_even(number) \
        :
    if number % 2 == 0:
        return True
    else:
        return False


def chess_board():
    height = 8
    width = 8

    x_coord_list = ['A','B','C','D','E','F','G','H']
    is_xcoord_printed = False

    for i in range(height):
        for j in range(width):

            if not is_xcoord_printed:
                for item in x_coord_list:
                    print(' ' + item, end=' ')
                print()
                is_xcoord_printed = True
            block = (i + j) % 2
            if block == 1:
                print("\033[7m   ", end="\033[0m")
            else:
                print("\033[0m   ", end='')

            if j == 8:
                print("   ")
        print()


if __name__ == '__main__':
    chess_board()
