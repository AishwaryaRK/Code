def are_meta_strings(s1, s2):
    if len(s1) != len(s2):
        return 0

    cnt = 0
    for a, b in zip(s1, s2):
        if a != b:
            cnt += 1
        if cnt > 2:
            return 0

    return 1 if cnt==2 else 0


t = int(input())
for i in range(0, t):
    s1 = input()
    s2 = input()
    print(are_meta_strings(s1, s2))
