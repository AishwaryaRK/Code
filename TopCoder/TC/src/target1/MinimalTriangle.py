import math


class MinimalTriangle:
    def maximalArea(self, length):
        return length * length * math.sqrt(3) / 4


print(MinimalTriangle().maximalArea(5))
