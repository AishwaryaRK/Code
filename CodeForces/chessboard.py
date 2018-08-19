import math


def get_chessboard_value(n, x, y):
    # k = 0
    # if (x + y) % 2 == 0:
    #     for i in range(1, x + 1):
    #         for j in range(1, y + 1):
    #             if i == x and j == y:
    #                 k += 1
    #                 return k
    #             if (i + j) % 2 == 0:
    #                 k += 1
    # for i in range(1, x + 1):
    #     for j in range(1, y + 1):
    #         if i == x and j == y:
    #             k += 1
    #             return math.ceil(n * n / 2) + k
    #         if (i + j) % 2 != 0:
    #             k += 1

    if n % 2 == 0:
        k = 0
        r1 = n / 2
        k += (x - 1) * r1
        k += math.floor((y - 1) / 2)
        if (x + y) % 2 == 0:
            # for i in range(1, y + 1):
            #     if (x + i) % 2 == 0:
            #         k += 1
            return int(k + 1)
        else:
            # for i in range(1, y + 1):
            #     if (x + i) % 2 != 0:
            #         k += 1
            return int(math.ceil(n * n / 2) + k + 1)
    else:
        k = 0
        r1 = r2 = -1
        if (x + y) % 2 == 0:
            r1 = math.ceil(n / 2)
            r2 = math.floor(n / 2)
        else:
            r1 = math.floor(n / 2)
            r2 = math.ceil(n / 2)
        k += math.ceil((x - 1) / 2) * r1
        k += math.floor((x - 1) / 2) * r2
        k += math.floor((y - 1) / 2)
        if (x + y) % 2 == 0:
            # for i in range(1, y + 1):
            #     if (x + i) % 2 == 0:
            #         k += 1
            return int(k + 1)
        else:
            # for i in range(1, y + 1):
            #     if (x + i) % 2 != 0:
            #         k += 1
            return int(math.ceil(n * n / 2) + k + 1)


# n, q = map(int, input().split())
# for i in range(0, q):
#     x, y = map(int, input().split())
#     print(get_chessboard_value(n, x, y))

print(get_chessboard_value(math.pow(10,9),math.pow(10,9),math.pow(10,9)))
