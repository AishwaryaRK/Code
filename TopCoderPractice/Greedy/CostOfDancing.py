class CostOfDancing:
    def minimum(self, k, dance_cost):
        return sum(sorted(dance_cost)[:k])


print(CostOfDancing().minimum(2, [1, 5, 3, 4]))
