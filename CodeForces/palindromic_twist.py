import math


def can_be_palindrome(l, s):
    for i in range(0, math.floor(l / 2)):
        if s[i] != s[-1 * (i + 1)]:
            if math.fabs(ord(s[i]) - ord(s[-1 * (i + 1)]))!= 2:
                return "NO"
    return "YES"


n = int(input())
for i in range(0, n):
    l = int(input())
    s = input()
    print(can_be_palindrome(l ,s))

print(can_be_palindrome(2, "ml"))
