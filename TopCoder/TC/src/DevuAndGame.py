class DevuAndGame:
    def canWin(self, nextLevel):
        visited = [0]
        currentLocation = 0
        while True:
            currentLocation = nextLevel[currentLocation]
            if currentLocation in visited:
                return "Lose"
            if currentLocation == -1:
                return "Win"
            visited.append(currentLocation)


print DevuAndGame().canWin((0, 1, 2))
