class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        ans = [1] * l
        left = [1] * l + 2
        right = [1] * l + 2
        for i in range(0, l):
            left[i + 1] = left[i] * nums[i]
            right[l - i] = right[l - i + 1] * nums[l - i - 1]
        for i in range(0, l):
            ans[i] = left[i - 1] * right[i + 1]
        return ans
