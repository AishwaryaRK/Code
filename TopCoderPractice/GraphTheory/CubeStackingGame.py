class CubeStackingGame:
    def MaximumValue(self, n, c1, c2, c3, c4):
        cubes = []
        for a, b, c, d in zip(c1, c2, c3, c4):
            cubes.append([a, b, c, d])
        print(cubes)

        max_ht = 0
        ht = 0
        stack = []
        for cube in cubes:
            for i in range(1, 8 + 1):
                stack.append(cube)
                if self.is_correct_stack(stack):
                    ht += 1
                    max_ht += 1
                    break
                else:
                    stack.pop()
                    if i == 8:
                        return len(stack)
                    if i == 5:
                        cube.reverse()
                    cube = self.rotate(cube)

        return len(stack)

    def rotate(self, cube):
        return cube[1:] + [cube[0]]

    def is_correct_stack(self, stack):
        for l in list(map(list, zip(*stack))):
            if len(l) != len(set(l)):
                return False
        return True


print(CubeStackingGame().MaximumValue(4, [1, 1, 3, 4], [1, 2, 3, 4], [1, 3, 3, 4], [1, 4, 3, 4]
                                      ))
