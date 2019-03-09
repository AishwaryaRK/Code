def can_grid_escape(n, r, c, k):
    if k == 0 and r == c == 1:
        print("Case #" + str(n) + ": IMPOSSIBLE")
        return

    if (k % c != 0 and k % r != 0) and k == (r - 1) * c - 1:
        print("Case #" + str(n) + ": IMPOSSIBLE")
        return

    if k % c == 0 and r - (k / c) < 2:
        print("Case #" + str(n) + ": IMPOSSIBLE")
        return

    if k % r == 0 and c - (k / r) < 2:
        print("Case #" + str(n) + ": IMPOSSIBLE")
        return

    print("Case #" + str(n) + ": POSSIBLE")

    cnt = 0

    if k % r == 0:
        print("1")
        for i in range(0, r):
            directions = ""
            for j in range(0, c):
                if cnt < k and j < k / c:
                    directions += 'S'
                    cnt += 1
                elif j == c - 1 and i == r - 2:
                    directions += 'W'
                elif j == c - 1 and i == r - 1:
                    directions += 'N'
                elif j < c - 1 and i == r - 1:
                    directions += 'E'
                else:
                    directions += 'S'
            print(directions)

    elif k % c == 0:
        print("2")
        for i in range(0, r):
            directions = ""
            for j in range(0, c):
                if cnt < k and i < k / r:
                    directions += 'W'
                    cnt += 1
                elif i == r - 1 and j < c - 1:
                    directions += 'E'
                elif i == r - 1 and j == c - 1:
                    directions += 'N'
                elif i == r - 2 and j == c - 1:
                    directions += 'W'
                else:
                    directions += 'S'
            print(directions)

    else:
        for i in range(0, r):
            directions = ""
            for j in range(0, c):
                if cnt < k:
                    if i == 0:
                        directions += 'W'
                    else:
                        directions += 'N'
                    cnt += 1
                else:
                    if i == r - 1 and j < c - 1:
                        directions += 'E'
                    elif i == r - 1 and j == c - 1:
                        directions += 'N'
                    elif i == r - 2 and j == c - 1:
                        l = len(directions)
                        d = directions[l - 1]
                        if d == 'N' or d == 'E':
                            directions += 'S'
                    else:
                        directions += 'S'
            print(directions)


T = int(input())
for n in range(1, T + 1):
    r, c, k = map(int, input().split(" "))
    can_grid_escape(n, r, c, k)
