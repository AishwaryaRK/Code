import heapq


def kthSmallest(matrix, k):
    # i = 1
    # j = len(matrix[0])
    # while i <= j:
    #     mid = int(i + (j - i) / 2)
    #     if mid * mid == k:
    #         return matrix[mid - 1][mid - 1]
    #     if mid * mid > k:
    #         if (mid - 1) * (mid - 1) < k:
    #             index = mid - 1
    #             break
    #         else:
    #             j = mid - 1
    #     elif mid * mid < k:
    #         i = mid + 1
    #
    # n = index * index + 1
    # c = 0
    # r = 0
    # print(index)
    # while True:
    #     if matrix[index][c] <= matrix[r][index]:
    #         m = matrix[index][c]
    #         c += 1
    #     else:
    #         m = matrix[r][index]
    #         r += 1
    #     if n == k:
    #         return m
    #     n += 1

    # print(kthSmallest([
    #     [1, 5, 9],
    #     [10, 11, 13],
    #     [12, 13, 15]
    # ], 8))

    h = []
    for j in range(0, len(matrix[0])):
        heapq.heappush(h, (matrix[0][j], 0, j))

    ans = None
    for i in range(0, k):
        n = heapq.heappop(h)
        ans = n[0]
        r = n[1]
        c = n[2]
        if r + 1 < len(matrix):
            heapq.heappush(h, (matrix[r + 1][c], r + 1, c))
heapq.
    return ans


print(kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 3))
