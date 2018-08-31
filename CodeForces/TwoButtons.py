def get_min_operations(n, m):
    if m == n:
        return 0
    if m < n:
        return n - m
    cnt = 0
    while m >= n:
        if m == n:
            return cnt
        if m % 2 != 0:
            cnt += 1
            m += 1
        else:
            if m / 2 < n:
                return cnt + 1 + n - int(m / 2)
            cnt += 1
            m /= 2

    return cnt


# n, m = map(int, input().split())
# print(get_min_operations(n, m))

print(get_min_operations(99, 100))
