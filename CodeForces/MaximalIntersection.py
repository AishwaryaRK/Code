from operator import itemgetter


def get_max_intersection_wo_1(n, segments):
    x = max(segments, key=itemgetter(0))[0]
    y = min(segments, key=itemgetter(1))[1]
    max_intersection = y - x
    # if max_intersection > 0:
    #     min_right = min(segments, key=itemgetter(1))[1]
    #     max_left = max(segments, key=itemgetter(0))[0]
    #     d1 = min_right - x
    #     d2 = y - max_left
    #     return max(d1, d2)
    # else:
    sorted(segments, key=lambda element: (element[0]))
    flag = False
    for i in range(0, n - 1):
        if segments[i][1] >= segments[i + 1][0]:
            flag = True
            break
    if not flag:
        return 0

    max_intersection = 0
    for i, segment in enumerate(segments):
        s = segments[:i] + segments[i + 1:]
        x = max(s, key=itemgetter(0))[0]
        y = min(s, key=itemgetter(1))[1]
        m = y - x
        if m > max_intersection:
            max_intersection = m


    return max_intersection

n = int(input())
segments = []
for i in range(0, n):
    a, b = map(int, input().split())
    segments.append((a, b))
print(get_max_intersection_wo_1(n, segments))

# print(get_max_intersection_wo_1(3, [(1, 5), (3, 10), (3, 5)]))
