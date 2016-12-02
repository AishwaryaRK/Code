class BearCheats:
    def eyesight(self, A, B):
        count = 0
        for a, b in zip(str(A), str(B)):
            if a != b:
                count += 1
        return "glasses" if count > 1 else "happy"


print BearCheats().eyesight(587, 697)
