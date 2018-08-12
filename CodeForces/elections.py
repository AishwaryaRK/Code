def get_min_bribe(voted_party_and_bribe):
    voted_party_and_bribe.sort(key=lambda tuple: tuple[1])
    # print(voted_party_and_bribe)

    bribes = {}
    max_party = 1
    max_cnt = 0
    for a in voted_party_and_bribe:
        if a[0] in bribes:
            b = bribes[a[0]]
        else:
            b = []
        b.append(a[1])
        bribes[a[0]] = b
        if len(b) >= max_cnt and a[0] != 1:
            max_party = a[0]
            max_cnt = len(b)

    # print(bribes, max_party)

    if 1 in bribes and len(bribes[1]) > max_cnt:
        return 0

    l = len(bribes[1]) if 1 in bribes else 0
    required = max_cnt - l + 1

    min_bribe = 0
    cnt = 0
    max_party_bribes = bribes[max_party]
    for i, v in enumerate(voted_party_and_bribe):
        if v[0] != 1 and v[0] != max_party:
            min_bribe += v[1]
            cnt += 1
            if cnt <= required - 2 and i < len(voted_party_and_bribe) - 2 - 1:
                if min_bribe + max_party_bribes[0] < min_bribe + voted_party_and_bribe[i + 1][1] + \
                        voted_party_and_bribe[i + 2][1]:
                    required -= 1
                    cnt += 1
                    min_bribe += max_party_bribes[0]
                    max_party_bribes.pop(0)
            if cnt == required:
                return min_bribe

    return min_bribe


# n, m = map(int, input().split())
# voted_party_and_bribe = []
# for i in range(0, n):
#     p, c = map(int, input().split())
#     voted_party_and_bribe.append((p, c))
# print(get_min_bribe(voted_party_and_bribe))


print(get_min_bribe([(2, 100), (3, 200), (4, 300), (5, 400), (5, 900)]))
