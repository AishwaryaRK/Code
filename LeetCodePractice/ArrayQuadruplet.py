def find_array_quadruplet(arr, s):
    if len(arr) < 4:
        return []

    arr = sorted(arr)

    ans = []
    flag = False
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            sum1 = arr[i] + arr[j]
            s1 = s - sum1
            x, y = get_index_of_remaining_sum(arr, s1, i, j)
            if x != -1 and y != -1:
                ans.append(sorted([arr[i], arr[j], arr[x], arr[y]]))
                flag = True

    if not flag:
        return []

    return sorted(ans, key=lambda e: (e[0], e[1], e[2], e[3]))[0]


def get_index_of_remaining_sum(arr, s1, i, j):
    x = 0
    y = len(arr) - 1
    while x < y:
        if x not in [i, j] and y not in [i, j]:
            s = arr[x] + arr[y]
            if s == s1:
                return x, y
            if s > s1:
                y -= 1
            else:
                x += 1
        if x in [i, j]:
            x += 1
        if y in [i, j]:
            y -= 1
    return -1, -1

    # 1 3 5 6 7 8 9 11 12  


