import math
class BearNSWE:
    def totalDistance(self, a, dir):
        current = {'x': 0, 'y': 0}
        totalDistance = 0
        for distance, direction in zip(a, dir):
            if direction == 'N':
                current['y'] = current['y'] + distance
            elif direction == 'S':
                current['y'] = current['y'] - distance
            elif direction == 'E':
                current['x'] = current['x'] + distance
            elif direction == 'W':
                current['x'] = current['x'] - distance
            totalDistance = totalDistance + distance
        totalDistance = totalDistance + math.sqrt(current['x'] * current['x'] + current['y'] * current['y'])
        return totalDistance


print(BearNSWE().totalDistance((1, 3, 3), "NES"))
