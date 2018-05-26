class Solution:
    def length_of_longest_substring(self, s):
        l = 0
        for i in range(0, len(s)):
            a = s[i]
            k = i + 1
            for j in range(i + 1, len(s)):
                if s[j] in a:
                    k = j
                    break
                a += s[j]
                k = j+1
            l = len(s[i:k]) if (len(s[i:k]) > l) else l

        return l


print(Solution().length_of_longest_substring("au"))
