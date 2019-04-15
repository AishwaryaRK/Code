import pprint

pp = pprint.PrettyPrinter(indent=2)


def setZeroes(matrix):
    m = len(matrix)
    if m == 0:
        return
    n = len(matrix[0])

    is_first_row_zero = False
    is_first_col_zero = False

    for r, row in enumerate(matrix):
        for c, e in enumerate(row):
            if e == 0:
                matrix[r][0] = None
                matrix[0][c] = None
                if c == 0:
                    is_first_col_zero = True
                if r == 0:
                    is_first_row_zero = True

    c = 1
    if is_first_col_zero:
        c = 0
    for i in range(c, n):
        if matrix[0][i] == None:
            for j in range(0, m):
                if i == 0 and matrix[0][0] == None and not is_first_row_zero:
                    matrix[0][0] = 0
                    continue
                if i == 0 and matrix[j][i] == None:
                    continue
                matrix[j][i] = 0
    r = 1
    if is_first_row_zero:
        r = 0
    for i in range(r, m):
        if matrix[i][0] == None:
            for j in range(0, n):
                matrix[i][j] = 0

    pp.pprint(matrix)


# setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
# setZeroes([[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]])
setZeroes([[1, 1, 1], [0, 1, 2]])
