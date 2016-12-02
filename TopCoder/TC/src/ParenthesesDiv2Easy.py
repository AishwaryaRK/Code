class ParenthesesDiv2Easy:
    def getDepth(self, s):
        depth = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                depth = count if count > depth else depth
                count = 0
        return depth


print(ParenthesesDiv2Easy().getDepth("(())()"))
