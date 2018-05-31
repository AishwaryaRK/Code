def get_next_empty_cell(m):
    for i in range(0, 9):
        for j in range(0, 9):
            if m[i][j] == 0:
                return i, j
    return -1, -1


def is_valid_sudoku(m):
    for row in m:
        row_without_zero = list(filter(lambda e: e != 0, row))
        if len(set(row_without_zero)) != len(row_without_zero):
            return False

    for j in range(0, 9):
        col = []
        for i in range(0, 9):
            if m[i][j] != 0:
                col.append(m[i][j])
        if len(set(col)) != len(col):
            return False

    i = 0
    while i < 9:
        j = 0
        while j < 9:
            block = []
            for x in range(0, 3):
                for y in range(0, 3):
                    if m[i + x][j + y] != 0:
                        block.append(m[i + x][j + y])
            if len(set(block)) != len(block):
                return False
            j += 3
        i += 3

    return True


def is_possible_sudoku(m):
    # print_matrix(m)
    i, j = get_next_empty_cell(m)
    if i == -1:
        return 1

    for v in range(1, 10):
        m[i][j] = v
        if is_valid_sudoku(m):
            m_copy = [row[:] for row in m]
            if is_possible_sudoku(m_copy) == 1:
                return 1

    return 0


import pprint


def print_matrix(m):
    pp = pprint.PrettyPrinter()
    pp.pprint(m)


t = int(input())
for i in range(0, t):
    s = list(map(int, input().strip().split(' ')))
    m = []
    for j in range(0, 9):
        row = []
        for k in range(0, 9):
            row.append(s[9 * j + k])
        m.append(row)
    print(is_possible_sudoku(m))
