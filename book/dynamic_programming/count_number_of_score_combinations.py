def count_number_of_score_combinations(points, score):
    if len(points) == 0:
        return 0
    if len(points) == 1:
        return 1 if score % points[0] == 0 else 0
    cnt = 0
    i = 0
    point = points[0]
    while point * i <= score:
        s = score - point * i
        if s == 0:
            cnt += 1
        else:
            c = count_number_of_score_combinations(points[1:], s)
            if c != 0:
                cnt += c
        i += 1
    return cnt


print(count_number_of_score_combinations([2, 3, 7], 12))
