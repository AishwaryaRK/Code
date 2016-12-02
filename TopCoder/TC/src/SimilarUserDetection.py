class SimilarUserDetection:
    def isSameGroup(self, c1, c2):
        group1 = ('0', 'O')
        group2 = ('1', 'l', 'I')
        if (c1 in group1 and c2 in group1) or (c1 in group2 and c2 in group2):
            return True
        return False

    def areSimilar(self, handle1, handle2):
        if len(handle1) != len(handle2):
            return False
        for c1, c2 in zip(handle1, handle2):
            if c1 != c2 and not self.isSameGroup(c1, c2):
                return False
        return True

    def haveSimilar(self, handles):
        for i in range(0, len(handles) - 1, 1):
            for j in range(i + 1, len(handles), 1):
                if self.areSimilar(handles[i], handles[j]):
                    return "Similar handles found"
        return "Similar handles not found"


print SimilarUserDetection().haveSimilar(("top", "coder", "TOPCODER", "TOPC0DER"))
