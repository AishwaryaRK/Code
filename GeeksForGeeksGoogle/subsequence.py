def longest_subsequence(s, list):
    longest_subsequence = ""
    for a in list:
        if len(a) > len(longest_subsequence):
            i = 0
            for c in a:
                while i < len(s):
                    if s[i] == c:
                        break
                    i += 1
                if i >= len(s):
                    break
            if i < len(s):
                longest_subsequence = a

    return longest_subsequence


t = int(input())
for i in range(0, t):
    input()
    list = input().split(' ')
    s = input()
    print(longest_subsequence(s, list))
