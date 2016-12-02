class ExplodingRobots:
    def canExplode(self, x1, y1, x2, y2, instructions):
        x = 0
        y = 0
        for instruction in instructions:
            if instruction == 'L' or instruction == 'R':
                x += 1
            if instruction == 'U' or instruction == 'D':
                y += 1
        return "Explosion" if (abs(x1 - x2) <= x and abs(y1 - y2) <= y) else "Safe"


print ExplodingRobots().canExplode(10, 5, -9, -10, "LULULULLLUULRULULULULULULLULULLULD")
