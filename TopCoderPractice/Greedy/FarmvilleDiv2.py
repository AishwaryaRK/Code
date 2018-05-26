class FarmvilleDiv2:
    def minTime(self, time, cost, budget):
        min_time = 0
        cost, time = zip(*sorted(zip(cost, time)))
        for t, c in zip(time, cost):
            if budget >= c:
                if budget >= t * c:
                    budget -= t * c
                else:
                    x = int(budget / c)
                    min_time += t - x
                    budget -= x * c
            else:
                min_time += t
            print(t, c, budget, min_time)
        return min_time


# class FarmvilleDiv2:
#     def minTime(self, time, cost, budget):
#         costTime = zip(cost, time)
#         costTime.sort()
#         time = [t for c, t in costTime]  # [x for y, x in sorted(zip(Y, X))]
#         cost = [c for c, t in costTime]
#         for index, c in enumerate(cost):
#             if c * time[index] <= budget:
#                 budget -= c * time[index]
#                 time[index] = 0
#             else:
#                 time[index] -= int(budget / c)
#                 break
#         return sum(time)
#
#
# print FarmvilleDiv2().minTime((1, 2, 3, 4, 5), (5, 4, 3, 2, 1), 15)

print(FarmvilleDiv2().minTime(
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],
    5000))
