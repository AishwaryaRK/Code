class Solution:
    def maxCoins(self, balloons):
        l = len(balloons)
        if l == 0:
            return 0
        max_coins = [[0] * l for i in range(l)]

        print(max_coins)
        for i in range(0, l):
            j = 0
            while j + i < l:
                a = None
                for k in range(j, j + i + 1):
                    b = 0
                    if k > j:
                        b += max_coins[j][k - 1]
                    if k < j + i:
                        b += max_coins[k + 1][j + i]
                    c = balloons[k]
                    if j - 1 >= 0:
                        c *= balloons[j - 1]
                    if j + i + 1 < l:
                        c *= balloons[j + i + 1]
                    b += c
                    if a == None or b > a:
                        a = b
                max_coins[j][j + i] = a
                j += 1
        print(max_coins)
        return max_coins[0][-1]


print(Solution().maxCoins([3, 1, 5, 8]))
print(Solution().maxCoins([]))
