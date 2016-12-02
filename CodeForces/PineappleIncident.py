def isPineappleIncident(t, s, x):
    return "YES" if x >= t and (x == t or (x - t) % s == 0 or ((x - t - 1) % s == 0 and x - t - 1 != 0)) else "NO"
    # if x == t:
    #     return "YES"
    # for i in range(1, int(x / s) + 1):
    #     if x == t + i * s or x == t + i * s + 1:
    #         return "YES"
    # return "NO"


t, s, x = map(int, input().split())
print(isPineappleIncident(t, s, x))
