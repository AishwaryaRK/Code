def max_friends_on_same_row(seats, S):
    count = 0
    for i in range(1, S + 1):
        r = 0
        for seat in seats:
            if seat[0] == i:
                r += 1
            elif seat[1] > seat[0] and seat[1] == i:
                r += 1
        if r > count:
            count = r

    return count


T = int(input())
for i in range(1, T + 1):
    F, S = map(int, input().split(" "))
    seats = []
    for j in range(0, F):
        r, c = map(int, input().split(" "))
        if (r, c) not in seats:
            seats.append((r, c))
    m = max_friends_on_same_row(seats, S)
    print("Case #" + str(i) + ": " + str(m))
