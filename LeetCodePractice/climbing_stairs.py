class Solution:
    def climbStairs(self, n):
        l = n
        number_of_ways = [None] * l
        for i in range(0, l):
            if i == 0:
                number_of_ways[i] = 1
            elif i == 1:
                number_of_ways[i] = 2
            else:
                number_of_ways[i] = number_of_ways[i - 1] + number_of_ways[i - 2]
        # print(number_of_ways)
        return number_of_ways[l-1]


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
