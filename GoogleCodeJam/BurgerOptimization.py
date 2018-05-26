def min_error(k, D):
    error = 0
    distances = []
    n = int(k / 2) - 1 if k % 2 == 0 else int((k - 1) / 2) - 1
    for i in range(0, n + 1):
        distances.append(i)
        distances.append(i)
    if k % 2 != 0:
        distances.append(int((k - 1) / 2))
    distances = sorted(distances, reverse=True)
    D = sorted(D, reverse=True)

    for d1, d2 in zip(D, distances):
        error += (d1 - d2) * (d1 - d2)

    return error


T = int(input())
for n in range(1, T + 1):
    k = int(input())
    optimal_distances = list(map(int, input().split(" ")))
    p = min_error(k, optimal_distances)
    print("Case #" + str(n) + ": " + str(p))
