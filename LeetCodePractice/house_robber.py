class Solution:
    def rob(self, nums):
        l = len(nums)
        money = [0] * (l + 1)
        for i, n in enumerate(nums):
            if i == 0:
                money[i + 1] = n
            else:
                money[i + 1] = max((n + money[i - 1]), (money[i]))
        return money[-1]


print(Solution().rob([2, 7, 9, 3, 1]))
