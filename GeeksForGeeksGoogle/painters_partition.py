# def time_taken_for_painting(k, n, board_sizes):
#     partitions = []
#     l = len(board_sizes)
#     j = 0
#     max_ele = max(board_sizes)
#     for i in range(0, k - 1):
#         sum = 0
#         while sum < max_ele and j < l:
#             sum += board_sizes[j]
#             j += 1
#         if sum >= max_ele:
#             partitions.append([sum, (j - 1)])
#         elif j >= l:
#             partitions.append([sum, l - 1])
#     if j < l:
#         sum = 0
#         while j < l:
#             sum += board_sizes[j]
#             j += 1
#         partitions.append([sum, (l - 1)])
#     print(partitions)
#     return

import math

def time_taken_for_painting(k, n, board_sizes):
    l = len(board_sizes)
    min_time = max(board_sizes)
    max_time = sum(board_sizes)
    while min_time < max_time:
        partition_cnt = 0
        approx_sum = math.floor((min_time + max_time) / 2)
        j = 0
        while j < l:
            s = 0
            while j < l and s + board_sizes[j] <= approx_sum:
                s += board_sizes[j]
                j += 1
            partition_cnt += 1
        if partition_cnt <= k:
            max_time = approx_sum
        if partition_cnt > k:
            min_time = approx_sum + 1
    return min_time


# t = int(input())
# for i in range(0, t):
#     k, n = map(int, input().strip().split(' '))
#     board_sizes = list(map(int, input().strip().split(' ')))
#     print(time_taken_for_painting(k, n, board_sizes))

print(time_taken_for_painting(3, 4, [10,50,5,5]))
