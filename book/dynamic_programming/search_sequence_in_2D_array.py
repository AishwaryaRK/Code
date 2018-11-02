def search_sequence_in_2D_array(grid, pattern):
    if len(pattern) == 0:
        return True
    start = None
    for i, row in enumerate(grid):
        for j, e in enumerate(row):
            if e == pattern[0]:
                start = (i, j)
    if start == None:
        return False

    return search_adjacent_entries(start, grid, pattern[1:])


def search_adjacent_entries(start, grid, pattern):
    i, j = start[0], start[1]
    if len(pattern) == 0:
        return True
    a = b = c = d = False
    if i > 0 and grid[i - 1][j] == pattern[0]:
        a = search_adjacent_entries((i - 1, j), grid, pattern[1:])
    if i < len(grid) - 1 and grid[i + 1][j] == pattern[0]:
        b = search_adjacent_entries((i + 1, j), grid, pattern[1:])
    if j > 0 and grid[i][j - 1] == pattern[0]:
        c = search_adjacent_entries((i, j - 1), grid, pattern[1:])
    if j < len(grid[0]) - 1 and grid[i][j + 1] == pattern[0]:
        d = search_adjacent_entries((i, j + 1), grid, pattern[1:])

    return a or b or c or d


print(search_sequence_in_2D_array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], [1, 3, 4, 6]))
