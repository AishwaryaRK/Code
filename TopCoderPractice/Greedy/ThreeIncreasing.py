class ThreeIncreasing:
    def minEaten(self, a, b, c):
        eaten = 0
        if b >= c:
            d1 = b - c + 1
            if b - d1 <= 1:
                return -1
            eaten += d1
            b -= d1
        print(a,b,c)
        if a >= b:
            d1 = a - b + 1
            if a - d1 < 1:
                return -1
            eaten += d1
        return eaten


print(ThreeIncreasing().minEaten(4,2,6))
