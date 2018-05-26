class LeftAndRightHandedDiv2:
    def count(self, S):
        c = 0
        for i, s in enumerate(S[1:]):
            if S[i] == 'R' and S[i + 1] == 'L':
                c += 1
        return c


print(LeftAndRightHandedDiv2().count("LRLRLR"))
