class InfiniteString:
    def equal(self, s, t):
        return "Equal" if self.getMinUnit(s) == self.getMinUnit(t) else "Not equal"

    def getMinUnit(self, str):
        subS = str[0]
        start = str[0]
        index = 1
        while index < len(str):
            if str[index] == start and (index + len(subS))<=len(str) and str[index:index + len(subS)] == subS:
                index += len(subS)
            else:
                subS = str[:index+1]
                index += 1
        return subS