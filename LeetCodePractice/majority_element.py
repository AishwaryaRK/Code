# Boyer-Moore Voting Algorithm - max freq element - time O(n), space O(1)

class Solution:
    def majorityElement(self, numbers):
        flag = True
        m = 0
        sum = 0
        for i, n in enumerate(numbers):
            if flag:
                m = n
                flag = False
            if n == m:
                sum += 1
            else:
                sum -= 1
            if sum == 0:
                flag = True
                sum = 0
        return m

print(Solution().majorityElement([2,2,1,1,1,2,2]))