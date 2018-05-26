class LittleElephantAndDouble:
    def getAnswer(self, A):
        A = sorted(A, reverse=True)
        for a in A:
            while a > A[-1]:
                a /= 2
            if a!=A[-1]:
                return "NO"
        return "YES"


print(LittleElephantAndDouble().getAnswer([1,2,3]))
