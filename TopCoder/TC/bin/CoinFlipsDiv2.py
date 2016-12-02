class CoinFlipsDiv2:
    def countCoins(self, state):
        count = 0
        for index, coin in enumerate(state):
            if (index - 1 >= 0 and state[index - 1] != coin) or (index + 1 < len(state) and state[index + 1] != coin):
                count += 1
        return count


print CoinFlipsDiv2().countCoins("HHTHHH")
