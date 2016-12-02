class TheKingsArmyDiv2:
    def getNumber(self, state):
        single_H_present = False
        for row in state:
            if "HH" in row:
                return 0
            if "H" in row:
                single_H_present = True
        for i in range(0, len(state[0])):
            col = "".join(map(lambda x: x[i], state))
            if "HH" in row:
                return 0
        if single_H_present:
            return 1
        return 2


print(TheKingsArmyDiv2().getNumber(["SSSSS", "SSHSS", "SSHSS"]))
