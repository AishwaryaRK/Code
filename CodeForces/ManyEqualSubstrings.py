def get_s(k, t):
    str = palindrome(t)
    t += str * (k - 1)
    return t


def palindrome(t):
    # if t == t[::-1]:

    # i = 0
    # j = len(t) - 1
    # while i <= j:
    #     if i == j:
    #         return t[int(len(t) / 2):]
    #     if t[i] == t[j]:
    #         i += 1
    #         j -= 1
    #     else:
    #         return t[i:]

    c = t[-1]
    i = -2
    while i >= -1 * len(t):
        if t[i] == c:
            l = len(t[:i + 1])
            if t[:i + 1] == t[-1 * l:]:
                return t[i + 1:]
        else:
            i -= 1
    return t


# n, k = map(int, input().split())
# t = input()
# print(get_s(k, t))

print(get_s(4, "cat"))
