class FilipTheFrog:
    def countReachableIslands(self, positions, L):
        count = 0
        start = positions[0]
        positions = sorted(positions)
        startIndex = positions.index(start)
        current = start
        for position in positions[startIndex:]:
            if abs(position - current) > L:
                break
            count += 1
            current=position
        current = start
        for position in reversed(positions[:startIndex]):
            if abs(position - current) > L:
                break
            count += 1
            current=position
        return count


print (FilipTheFrog().countReachableIslands((4, 7, 1, 3, 5), 1))
