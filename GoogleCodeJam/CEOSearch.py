def min_ex(experiences, final, L):
    experiences = sorted(experiences, key=lambda tup: tup[1], reverse=True)
    final = sorted(final, key=lambda tup: tup[1], reverse=True)
    for i, ex in enumerate(experiences):
        j = i + 1
        power = ex[0] * ex[1]
        while j < len(experiences):
            if final[j][0] > 0:
                if final[j][0] >= power:
                    final[j][0] -= power
                    break
                else:
                    power -= final[j][0]
                    final[j][0] = 0
            j += 1
    count = 0
    for f in final:
        count += f[0]

    return count if count > final[0][1] + 1 else final[0][1] + 1


T = int(input())
for n in range(1, T + 1):
    L = int(input())
    experiences = []
    final = []
    for i in range(0, L):
        m, e = map(int, input().split(" "))
        experiences.append([m, e])
        final.append([m, e])
    ex = min_ex(experiences, final, L)
    print("Case #" + str(n) + ": " + str(ex))
