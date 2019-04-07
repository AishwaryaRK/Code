class Solution:

    # Input: [1,3,0,0,12], [1,0]
    # Output: [1,3,12,0,0]
    def moveZeroes(self, nums):
        l = len(nums)
        i = 0
        j = 0
        while j < l and i < l:
            if nums[j] != 0 and nums[i] == 0 and j > i:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            while i < l and nums[i] != 0:
                i += 1
            while j < l and (nums[j] == 0 or j <= i):
                j += 1


