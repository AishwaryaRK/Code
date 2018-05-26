def replace_chars(s):
    i = 0
    j = 0
    s = list(s)
    while j < len(s):
        if s[j] == 'b':
            j += 1
        elif s[j] == 'a' and j + 1 < len(s) and s[j + 1] == 'c':
            j += 2
        elif i < j:
            s[i] = s[j]
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    return ''.join(s[:i])


t = int(input())
for i in range(0, t):
    s = input()
    print(replace_chars(s))


