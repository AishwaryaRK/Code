def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not (s[i].isalpha() or s[i].isnumeric()) and i < j:
            i += 1
        while not (s[j].isalpha() or s[j].isnumeric()) and i < j:
            j -= 1
        if i >= j:
            break
        if s[i] != s[j]:
            return "NO"
        i += 1
        j -= 1
    return "YES"


t = int(input())
for i in range(0, t):
    s = input()
    print(is_palindrome(s.lower()))
