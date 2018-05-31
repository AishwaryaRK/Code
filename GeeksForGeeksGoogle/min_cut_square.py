memoization_cache = {}


def number_of_squares(n, m):
    if n == m:
        return 1
    if n == 1 or m == 1:
        return n * m

    key = str(n) + "-" + str(m)
    if key in memoization_cache:
        return memoization_cache[key]

    a = m * n
    for i in range(1, int(n / 2) + 1):
        a = min(a, number_of_squares(i, m) + number_of_squares(n - i, m))

    b = m * n
    for j in range(1, int(m / 2) + 1):
        b = min(b, number_of_squares(n, j) + number_of_squares(n, m - j))

    memoization_cache[key] = min(a, b)
    return min(a, b)


t = int(input())
for i in range(0, t):
    n, m = map(int, input().split(' '))
    print(number_of_squares(n, m))

print(number_of_squares(13, 29))
