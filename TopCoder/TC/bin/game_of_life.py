from pprint import pprint

board = [[False, False, False, False, False],
         [False, False, True, False, False],
         [False, False, True, False, False],
         [False, False, True, False, False],
         [False, False, False, False, False]]


def get_alive(board, row, col):
    neighbours = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
                  (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    valid_neightbours = [(r, c) for r, c in neighbours if 0 <= r <= 4 and 0 <= c <= 4]
    alive_neighbours = [(r, c) for r, c in valid_neightbours if board[r][c] == True]
    return len(alive_neighbours)


def get_new_cell(board, row, col):
    alive_neighbours = get_alive(board, row, col)
    if board[row][col] and alive_neighbours == 2 or alive_neighbours == 3:
        return True
    elif not board[row][col] and alive_neighbours == 3:
        return True
    else:
        return False


def evolve(board):
    return [[get_new_cell(board, row, col) for col in range(5)] for row in range(5)]


pprint (board)
new_board = evolve(board)
pprint(new_board)
