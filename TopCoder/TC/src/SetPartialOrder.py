class SetPartialOrder:
    def compareSets(self, a, b):
        a = sorted(a)
        b = sorted(b)
        if a == b:
            return "EQUAL"
        if len(a) > len(b) and len([e for e in b if e in a]) == len(b):
            return "GREATER"
        if len(a) < len(b) and len([e for e in a if e in b]) == len(a):
            return "LESS"
        return "INCOMPARABLE"


print(SetPartialOrder().compareSets((2, 3, 5, 7), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
