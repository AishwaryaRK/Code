def min_difference(fs, n):
    best = None
    i = 0
    l = len(fs)
    fs.sort()
    while i + n - 1 < l:
        d = fs[i + n - 1] - fs[i]
        if best == None or d < best:
            best = d
        i += 1
    return best


n, m = map(int, input().split())
fs = list(map(int, input().split()))
print(min_difference(fs, n))
