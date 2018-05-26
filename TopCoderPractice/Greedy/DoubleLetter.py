class DoubleLetter:
    def ableToSolve(self, S):
        while S:
            l = len(S)
            str = ""
            i = 0
            while i < l:
                if (i + 1 < l) and S[i] == S[i + 1]:
                    i += 2
                else:
                    str += S[i]
                    i += 1
            if S == str:
                return "Impossible"
            S = str

        return "Possible"


print(DoubleLetter().ableToSolve("aabccbb"))
