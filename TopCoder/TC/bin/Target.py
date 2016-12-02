from pprint import pprint


class Target:
    sqdims = []

    def draw(self, n):
        self.calcSqDims(n)
        return tuple("".join("#" if self.is_painted(i, j) else "" for j in range(0, n)) for i in range(0, n))

    def calcSqDims(self, n):
        for i in range(0, int(n / 2) + 1, 2):
            self.sqdims.append((i, i, n))
            n -= 4

    def is_painted(self, i, j):
        for (r, c, n) in self.sqdims:
            if r == i or r + n - 1 == i:
                if c <= j < r + n:
                    return True
            if c == j or c + n - 1 == j:
                if r <= i < c + n:
                    return True
        return False


pprint(Target().draw(9))
