def min_steps(x, y):
    if x != 0 and y != 0:
        return 2 * (abs(0 - x) + abs(0 - y))

    x = 1
    return 2 * (abs(0 - x) + abs(0 - y)) + 1


T = int(input())
for n in range(1, T + 1):
    x, y = map(int, input().split(" "))
    print(min_steps(x, y))
