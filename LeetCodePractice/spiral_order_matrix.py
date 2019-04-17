def spiralOrder(matrix):
    ans = []
    r = len(matrix)
    if r == 0:
        return ans
    c = len(matrix[0])
    iterations = int(r / 2) + 1

    a = True
    for i in range(0, iterations):
        # top
        if not a:
            break
        a = False
        for j in range(0 + i, c - i):
            ans.append(matrix[i][j])
            a = True

        # right
        if not a:
            break
        a = False
        for j in range(0 + i + 1, r - i):
            ans.append(matrix[j][c - i - 1])
            a = True

        # bottom reverse
        if not a:
            break
        a = False
        for j in range(c - i - 1 - 1, 0 + i - 1, -1):
            ans.append(matrix[r - i - 1][j])
            a = True

        # up reverse
        if not a:
            break
        a = False
        for j in range(r - i - 1 - 1, 0 + i, -1):
            ans.append(matrix[j][0 + i])
            a = True
    return ans


# print(spiralOrder([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]))

# print(spiralOrder([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]))

print(spiralOrder([[2, 5, 8], [4, 0, -1]]))
