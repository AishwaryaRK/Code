class BearPair:
    def bigDistance(self, s):
        distance = -1
        for i in range(0, len(s) - 1, 1):
            count = 0
            for j in range(len(s) - 1, i, -1):
                print s[i], s[j]
                if s[i] != s[j]:
                    count = j - i
                    distance = count if count > distance else distance
                    break
        return distance


print BearPair().bigDistance("qw")
