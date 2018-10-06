class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        x, y = 0, n - 1

        while True:
            t = matrix[x][y]
            if target == t:
                return True
            if target < t:
                if y - 1 < 0:
                    return False
                y -= 1
            if target > t:
                if x + 1 >= m:
                    return False
                x += 1

        return False

    # def searchMatrix(self, matrix, target):
    #     m = len(matrix)
    #     if m == 0:
    #         return False
    #     n = len(matrix[0])
    #     if n == 0:
    #         return False
    #
    #     x, y = 0, 0
    #
    #     while True:
    #         t = matrix[x][y]
    #         if target == t:
    #             return True
    #         if target > t:
    #             if x + 1 < m and y + 1 < n:
    #                 x, y = x + 1, y + 1
    #             elif x + 1 >= m and y + 1 >= n:
    #                 return False
    #             elif x + 1 < m:
    #                 x += 1
    #                 # return target in matrix[x + 1]
    #             elif y + 1 < n:
    #                 y += 1
    #                 # array = [row[y] for row in matrix]
    #                 # if target in array:
    #                 #     return
    #         if target < t:
    #             array1 = [r for i, r in enumerate(matrix[x]) if i < y]
    #             array2 = [row[y] for i, row in enumerate(matrix) if i < x]
    #             return target in array1 or target in array2
    #     return False


print(Solution().searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 20))
print(Solution().searchMatrix([[-5]], 2))
print(Solution().searchMatrix([[1, 3, 5]], 5))
print(Solution().searchMatrix([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]], 15))
