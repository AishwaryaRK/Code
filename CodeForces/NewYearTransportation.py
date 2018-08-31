def is_transport_possible(t, portals):
    i = 1
    while True:
        i += portals[i-1]
        if i == t:
            return "YES"
        if i > t:
            return "NO"

    return "NO"


n, t = map(int, input().split())
portals = list(map(int, input().split()))
print(is_transport_possible(t, portals))
