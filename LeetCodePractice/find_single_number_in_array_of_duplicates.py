class Solution:
    def singleNumber(self, nums):
        ans = nums[0]
        for n in nums[1:]:
            ans = ans ^ n
        return ans
