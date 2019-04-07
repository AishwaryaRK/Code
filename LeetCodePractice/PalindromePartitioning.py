def partition(s):
    partitions = []
    for i in range(1, len(s)):
        stack = [([], s)]
        while len(stack) != 0:
            p = stack.pop()
            p1 = p[0]
            p2 = p[1]
            if p2 == "":
                partitions.append(p1)
            else:
                for j in range(0, len(p2) - i + 1):
                    a = p2[j:j + i]
                    if is_palindrome(a):
                        # print(p1, p2)
                        stack.append((p1 + [a], p2[j + i:]))
                    stack.append((p1 + [p2[j]], p2[j + 1:]))
        print(partitions)
        print("**********************************************************")
    return partitions

def is_palindrome(a):
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] != a[j]:
            return False
        i += 1
        j -= 1
    return True

print(partition("aab"))
