import collections


def longestSubstring(s, k):
    # ans = []
    # for i, c in enumerate(s):
    #     if i == 0:
    #         ans.append({c: 1})
    #     else:
    #         a = ans[i - 1].copy()
    #         v = 1
    #         if c in a:
    #             v = a[c] + 1
    #         a[c] = v
    #         ans.append(a)
    # for i in range(len(ans) - 1, -1, -1):
    #     if all(v >= k for v in ans[i].values()):
    #         return sum(ans[i].values())
    #
    # return 0

    if len(s) < k:
        return 0

    freq = collections.Counter(s)
    for c, f in freq.items():
        if f < k:
            return max(longestSubstring(str, k) for str in s.split(c))

    return len(s)


# print(longestSubstring('ababbc', 2))
print(longestSubstring("bbaaacbd", 3))
