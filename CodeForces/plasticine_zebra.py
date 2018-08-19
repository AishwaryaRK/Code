def zebra_len(s):
    max_len = get_max_len(s)
    for i in range(1, len(s)):
        if s[0] != s[-1]:
            s1 = s[:i]
            s2 = s[i:]
            s1 = s1[::-1]
            s2 = s2[::-1]
            s3 = s1 + s2
            m = get_max_len(s3)
            if m > max_len:
                max_len = m
                s = s3

    return max_len


def get_max_len(s):
    max_len = None
    c = 1
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            if max_len == None or c > max_len:
                max_len = c
            c = 1
        else:
            c += 1
        prev = s[i]

    return max_len


s = input()
print(zebra_len(s))
