def count_uber(ubers):
    ubers = sorted(ubers, key=lambda x: x[0])
    min = ubers[0][0]
    max = ubers[0][1]
    count = 0
    for uber in ubers:
        if max < uber[0]:
            count += max - min + 1
            min = uber[0]
            max = uber[1]
        elif max < uber[1]:
            max = uber[1]

    count += max - min + 1
    return count


N = int(input())
ubers = list()
for i in range(0, N):
    ubers.append(tuple(map(int, input().strip().split(' '))))
print(count_uber(ubers))
