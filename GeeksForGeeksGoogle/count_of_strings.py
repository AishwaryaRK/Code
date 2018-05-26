def count(n):
    return int(1 + n + n + (n * (n - 1)) + (n * (n - 1) * (n - 2) / 2) + (n * (n - 1) / 2))


t = int(input())
for i in range(0, t):
    n = int(input())
    print(count(n))
