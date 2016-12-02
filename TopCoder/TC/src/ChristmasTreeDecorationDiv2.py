class ChristmasTreeDecorationDiv2:
    def solve(self, col, x, y):
        ans = 0
        for a, b in zip(x, y):
            if col[a - 1] != col[b - 1]:
                ans += 1
        return ans

    