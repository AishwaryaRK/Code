import math


def get_distance(t1, f1, t2, f2, a, b):
    if t1 == t2:
        return int(math.fabs(f2 - f1))
    d = int(math.fabs(t1 - t2))
    h = f1
    if f1 > b:
        d += f1 - b
        h = b
    elif f1 < a:
        d += a - f1
        h = a
    if f2 != h:
        d += int(math.fabs(f2 - h))
    return d


n, h, a, b, k = map(int, input().split())
for i in range(0, k):
    t1, f1, t2, f2 = map(int, input().split())
    print(get_distance(t1, f1, t2, f2, a, b))
