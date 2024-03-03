def is_even(number) \
        :
    if number % 2 == 0:
        return True
    else:
        return False


def chess_board():
    height = 8
    width = 8
    for i in range(height):
        for j in range(width):

            block = (i + j) % 2
            if block == 1:
                print(u"\u2B1B", end=' ')
            else:
                print(u"\u2B1C", end=' ')

        print()


if __name__ == '__main__':
    chess_board()
