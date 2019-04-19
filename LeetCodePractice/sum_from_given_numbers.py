def numSquares(n):
    sq = []
    for i in range(1, n+1):
        if i * i <= n:
            sq.append(i * i)
        else:
            break

    return getCount(n, sq)


def getCount(n, sq):
    if n == 0:
        return 0
    return 1 + min(getCount(n - s, sq) for s in sq if s <= n)


print(numSquares(39))
