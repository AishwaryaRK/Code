# coins = [1, 2, 5], amount = 11
# 11 = 5 + 5 + 1

def coinChange(coins, amount):
    coins.sort()
    ans = [0] * (amount + 1)
    for r, coin in enumerate(coins):
        for c in range(1, amount + 1):
            if c < coin:
                if r == 0:
                    ans[c] = -1
            else:
                v = ans[c - coin]
                if v == -1:
                    if r == 0:
                        ans[c] = -1
                else:
                    if r == 0:
                        ans[c] = 1 + v
                    else:
                        v1 = ans[c]
                        ans[c] = 1 + min(v, v1)

    return ans[-1]


print(coinChange([83, 186, 408, 419], 6249))
# ans=20