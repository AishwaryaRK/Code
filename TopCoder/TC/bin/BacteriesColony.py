class BacteriesColony:
    def performTheExperiment(self, colonies):
        new_colonies = None
        while colonies != new_colonies:
            if new_colonies == None:
                new_colonies = list(colonies)
            colonies = list(new_colonies)
            for i in range(1, len(colonies) - 1):
                if colonies[i + 1] > colonies[i] and colonies[i - 1] > colonies[i]:
                    new_colonies[i] = colonies[i] + 1
                elif colonies[i + 1] < colonies[i] and colonies[i - 1] < colonies[i]:
                    new_colonies[i] = colonies[i] - 1
        return new_colonies


print(BacteriesColony().performTheExperiment([5, 3, 4, 6, 1]))
