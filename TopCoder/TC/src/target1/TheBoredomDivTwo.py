class TheBoredomDivTwo:
    def find(self, n, m, j, b):
        cnt = n
        if j > n:
            cnt += 1
        if b > n:
            cnt += 1
        return cnt


print(TheBoredomDivTwo().find(1, 1, 1, 2))
