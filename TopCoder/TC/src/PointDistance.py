class PointDistance:
    def findPoint(self, x1, y1, x2, y2):
        x3 = 100 if x2 >= x1 else -100
        y3 = 100 if y2 >= y1 else -100
        return (x3, y3)


print(PointDistance().findPoint(0, 1, 2, 3))
