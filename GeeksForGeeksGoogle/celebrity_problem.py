def getID(M, n):
    for i,row in enumerate(M):
        if all(c == 0 for c in row):
            is_celebrity=True
            for j,row in enumerate(M):
                if j!=i and row[i]!=1:
                    is_celebrity=False
                    break
            if is_celebrity:
                return i

    return -1


M = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
print(getID(M, 3))
