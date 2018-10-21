class Solution:
    def minCostClimbingStairs(self, cost):
        l = len(cost)
        min_costs = [None] * l
        for i in range(0, l):
            if i <= 1:
                min_costs[i] = cost[i]
            else:
                min_costs[i] = cost[i] + min(min_costs[i - 1], min_costs[i - 2])
        return min(min_costs[-1], min_costs[-2])


print(Solution().minCostClimbingStairs([10, 15, 20]))
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
