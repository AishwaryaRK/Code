def replace_o_with_x(mat, n, m):
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            queue = []
            indices = []
            if mat[i][j] == 'O':
                queue.append((i, j))
                indices.append((i, j))
                while len(queue) != 0:
                    (x, y) = queue.pop(0)
                    if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                        indices = []
                        break
                    if x > 0 and mat[x - 1][y] == 'O':
                        queue.append((x - 1, y))
                        indices.append((x - 1, y))
                    if x < n - 1 and mat[x + 1][y] == 'O':
                        queue.append((x + 1, y))
                        indices.append((x + 1, y))
                    if y > 0 and mat[x][y - 1] == 'O':
                        queue.append((x, y - 1))
                        indices.append((x, y - 1))
                    if y < m - 1 and mat[x][y + 1] == 'O':
                        queue.append((x, y + 1))
                        indices.append((x, y + 1))
                for v in indices:
                    mat[v[0]][v[1]] = 'X'

    return mat


t = int(input())
for i in range(0, t):
    n, m = map(int, input().split(' '))
    s = input().strip().split(' ')
    mat = []
    for j in range(0, n):
        row = []
        for k in range(0, m):
            row.append(s[m * j + k])
        mat.append(row)
    mat = replace_o_with_x(mat, n, m)
    for row in mat:
        print(*row, end=' ')
