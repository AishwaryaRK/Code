def is_middle(L, names):
    s = ["", "", ""]
    n0 = names[0]
    n1 = names[1]
    n2 = names[2]

    i = 0
    while n0[i] == n1[i] == n2[i]:
        i += 1

    ch_same = ""
    ch_diff = ""

    while i < L:
        check_names = []
        for j, a in enumerate(s):
            if not a:
                check_names.append([names[j], j])
        letters = [name[0][i] for name in check_names]
        unique_letters = set(letters)
        if len(unique_letters) == len(letters):
            if not letters:
                break
            if len(unique_letters) == 3:
                for j, a in enumerate(s):
                    if not a:
                        s[j] = "YES"
                break

            if check_names[0][0][i] == ch_same and check_names[1][0][i] == ch_diff:
                s[check_names[0][1]] = "NO"
                s[check_names[1][1]] = "YES"
            elif check_names[1][0][i] == ch_same and check_names[0][0][i] == ch_diff:
                s[check_names[1][1]] = "NO"
                s[check_names[0][1]] = "YES"
            else:
                s[check_names[0][1]] = "YES"
                s[check_names[1][1]] = "YES"
            break
        elif len(unique_letters) == 2:
            if n0[i] == n1[i] and n1[i] != n2[i] and s[2] == "":
                s[2] = "NO"
                ch_diff = n2[i]
                ch_same = n0[i]
            elif n1[i] == n2[i] and n2[i] != n0[i] and s[0] == "":
                s[0] = "NO"
                ch_diff = n0[i]
                ch_same = n1[i]
            elif n2[i] == n0[i] and n0[i] != n1[i] and s[1] == "":
                s[1] = "NO"
                ch_diff = n1[i]
                ch_same = n2[i]
        i += 1

    for i, a in enumerate(s):
        if not a:
            s[i] = "NO"

    return s


T = int(input())
for n in range(1, T + 1):
    L = int(input())
    names = input().split(" ")
    s = is_middle(L, names)
    print("Case #" + str(n) + ": " + " ".join(s))
