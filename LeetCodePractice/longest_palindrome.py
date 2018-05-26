class Solution:
    def longest_palindrome(self, s):
        ans = s[0]
        for i in range(0, len(s)):
            l1 = i
            j = len(s) - 1
            l2 = len(s) - 1
            while l2 >= l1:
                while l2 >= l1:
                    if s[l1] == s[l2]:
                        l1 += 1
                        l2 -= 1
                    else:
                        break
                print(i,j,l1, l2, len(s[i:j + 1]))
                if l2 < l1 and len(s[i:j + 1]) > len(ans):
                    ans = s[i:j + 1]
                    print(ans)
                else:
                    j -= 1
                    l2 = j
                    l1 = i
        return ans


print(Solution().longest_palindrome("cbbd"))
