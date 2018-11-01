def levenshtein_edit_distance(a, b):
    distances = [[0] * (len(a) + 1) for i in range(0, (len(b) + 1))]
    for i in range(0, len(a) + 1):
        distances[0][i] = i
    for i in range(0, len(b)):
        distances[i][0] = i
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            s = 0 if a[j - 1] == b[i - 1] else 1
            distances[i][j] = s + min(distances[i - 1][j - 1], distances[i - 1][j], distances[i][j - 1])

    return distances[-1][-1]


print(levenshtein_edit_distance("Carthorse", "Orchestra"))
