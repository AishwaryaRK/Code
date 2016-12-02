class ElectronicPetEasy:
    def isDifficult(self, st1, p1, t1, st2, p2, t2):
        a = [st1 + i * p1 for i in range(0, t1)]
        b = [st2 + i * p2 for i in range(0, t2)]
        if not set(a).intersection(b):
            return "Easy"
        return "Difficult"


ElectronicPetEasy().isDifficult(3, 3, 3, 5, 2, 3)
