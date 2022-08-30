grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def print_board(board):
    # Row
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("---------------------------")
        # Column
        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0:
                print(" | ", end="")
            if column == 8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")


def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)


def solver(board):
    find = find_empty(board)
    if not find:
        return True

    row, column = find  # position of empty place

    for i in range(1, 10):  # we try numbers from 1-9
        if is_valid(board, i, find):
            board[row][column] = i

            if solver(board):
                return True

        board[row][column] = 0

    return False


def is_valid(board, number, pos):
    # Check the row to see if a number can be entered and disregard the place where the number is entered
    for i in range(len(board)):
        if board[pos[0]][i] == number and pos[1] != i:
            return False

    # Check the column to see if a number can be entered and disregard the place where the number is entered
    for i in range(len(board[0])):
        if board[i][pos[1]] == number and pos[0] != i:
            return False

    # # # # # # # # # # # #
    #  [0,0] [0,1] [0,2]  #
    #  [1,0] [1,1] [2,2]  #
    #  [2,0] [2,1] [2,2]  #
    # # # # # # # # # # # #
    # Find position of the box

    start_x = pos[0] // 3  # row
    start_y = pos[1] // 3  # column

    # Check the box to see if a number can be entered and disregard the place where the number is entered
    for i in range(3):
        for j in range(3):
            if (
                board[start_x * 3 + i][start_y * 3 + i] == number
                and (start_x * 3 + i, start_y * 3 + i) != pos
            ):
                return False

    return True


solver(grid)

print_board(grid)
