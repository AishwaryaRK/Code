class GreaterGameDiv2:
    def calc(self, snuke, sothe):
        return sum(1 for a, b in zip(snuke, sothe) if a > b)


print(GreaterGameDiv2().calc({1, 3, 5}, {4, 2, 1}))
