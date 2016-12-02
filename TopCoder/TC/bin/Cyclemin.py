class Cyclemin:
    def bestmod(self, s, k):
        rotations = [s]
        for i in range(len(s) - 1):
            s = s[1:] + s[0]
            rotations.append(s)
        mutated_rotations = []
        for rotation in rotations:
            n = k
            for i, c in enumerate(rotation):
                if (n != 0 and c != 'a'):
                    rotation = rotation[:i] + 'a' + rotation[i + 1:]
                    n -= 1
            mutated_rotations.append(rotation)
        return min(mutated_rotations)


print(Cyclemin().bestmod("abacaba", 1))
