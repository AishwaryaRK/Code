def get_distinct_transformations(a, b):
    if a == b:
        return 1
    if len(a) < len(b):
        return 0

    deletion_indices = []
    j = 0
    for i, c in enumerate(a):
        if j >= len(b) or c != b[j]:
            deletion_indices.append(i)
            b = b[:j] + "-" + b[j:]
            j += 1
        else:
            j += 1

    print(a)
    print(b)

    product = 1
    j = len(deletion_indices) - 1
    i = deletion_indices[j]
    while j >= 0:
        if deletion_indices[j] <= i:
            i = deletion_indices[j]
            c = a[i]
            n = 1
            r = 1
            i -= 1
            while i >= 0:
                if a[i] == c:
                    n += 1
                    if b[i] == '-':
                        r += 1
                    i -= 1
                else:
                    break
            while n > r:
                product *= n
                n-=1
        j -= 1

    return product


# t = int(input())
# for i in range(0, t):
#     a = input()
#     b = input()
#     print(get_distinct_transformations(a, b))

# print(get_distinct_transformations(
#     "wlrrrrbaakkaabmqbpphcdarzoccccwxllllxkkhhhhyllhiyyyyddqsbbppbcdqqxrjkkmoeeeewfrxseeej",
#     "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsj"))

print(get_distinct_transformations("zyxaoooocbhhkirrrmmmmcqcoooooendtomfgdwdwwwwwfcggqqqgpxiqvkuytdqqqlcgdewhta",
                                    "zyxacbhhkicqcoendtomfgdwdwfcgpxiqvkuytdlcgdewhta"))
