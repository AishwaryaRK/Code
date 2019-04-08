import random

# Fisher-Yates algorithm
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ans = self.nums[:]
        for i in range(0, len(ans)):
            j = random.randint(i-1, len(ans) - 1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans

# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
