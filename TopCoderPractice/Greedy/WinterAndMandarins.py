class WinterAndMandarins:
    def getNumber(self, bags, k):
        bags = sorted(bags)
        print(bags)
        count = bags[k - 1] - bags[0]
        print(k - 1, 0)
        i = 1
        while i + k <= len(bags):
            print(i + k - 1, i)
            if bags[i + k - 1] - bags[i] < count:
                count = bags[i + k - 1] - bags[i]
            i += 1
        return count


print(WinterAndMandarins().getNumber([5, 4, 6, 1, 9, 4, 2, 7, 5, 6], 4))
