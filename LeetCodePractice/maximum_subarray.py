# Kadane's Algorithm - max subarray sum

class Solution:
    def maxSubArray(self, numbers):
        max_sum = 0
        sums = []
        for i, n in enumerate(numbers):
            if i == 0:
                max_sum = n
                sums.append(n)
            else:
                s = sums[i - 1] + n
                if s < n:
                    s = n
                sums.append(s)
                if s > max_sum:
                    max_sum = s

        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
