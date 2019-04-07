class Solution:
    # [1, 2, 3]
    def permute(self, nums):
        ans = []
        stack = [([], nums)]
        while len(stack) != 0:
            n = stack.pop()
            a = n[0]
            b = n[1]
            l = len(b)
            if l != 0:
                for i in range(0, l):
                    stack.append((a + [b[i]], b[:i] + b[i + 1:]))
            else:
                ans.append(a)
        return ans
