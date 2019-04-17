def isToeplitz(arr):
    r = len(arr)
    c = len(arr[0])
    row = arr[0]
    for r in arr[1:]:
        if row[:-1] != r[1:]:
            return False
        row = r
    return True


print(isToeplitz([[1, 2, 3, 4],
                  [5, 1, 2, 3],
                  [6, 5, 1, 2]]))
print(isToeplitz([[1, 2, 3, 4],
                  [5, 1, 9, 3],
                  [6, 5, 1, 2]]))
