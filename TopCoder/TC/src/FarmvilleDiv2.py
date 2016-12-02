
class FarmvilleDiv2:
    def minTime(self, time, cost, budget):
        costTime = zip(cost, time)
        costTime.sort()
        time = [t for c, t in costTime]  # [x for y, x in sorted(zip(Y, X))]
        cost = [c for c, t in costTime]
        for index, c in enumerate(cost):
            if c * time[index] <= budget:
                budget -= c * time[index]
                time[index] = 0
            else:
                time[index] -= int(budget / c)
                break
        return sum(time)


print FarmvilleDiv2().minTime((1, 2, 3, 4, 5), (5, 4, 3, 2, 1), 15)
