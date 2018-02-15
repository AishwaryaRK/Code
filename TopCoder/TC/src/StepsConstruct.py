class StepsConstruct:
    reached = False

    def construct(self, board, k):
        if board[0][0] == '#':
            return ""
        current_pos = [0, 0]
        previous_pos = [-1, -1]
        path = []
        path = self.getPath(board, k, path, current_pos, previous_pos)
        path = ''.join(path)
        if len(path) == k and self.reached:
            return path
        return ""

    def getPath(self, board, k, path, current_pos, previous_pos):
        r = len(board)
        c = len(board[0])
        dest = [r - 1, c - 1]
        if k == 0 and current_pos == dest:
            self.reached = True
            return path
        if k == 0:
            return path
        i = current_pos[0]
        j = current_pos[1]
        options = []
        if i + 1 < r and [i + 1, j] != previous_pos:
            options.append([i + 1, j, 'D'])
        if j + 1 < c and [i, j + 1] != previous_pos:
            options.append([i, j + 1, 'R'])
        if j - 1 >= 0 and [i, j - 1] != previous_pos:
            options.append([i, j - 1, 'L'])
        if i - 1 >= 0 and [i - 1, j] != previous_pos:
            options.append([i - 1, j, 'U'])

        for option in options:
            m, n = option[0], option[1]
            if board[m][n] == '.':
                path.append(option[2])
                temp_path = list(path)
                test_path = self.getPath(board, k - 1, temp_path, [m, n], current_pos)
                # print "test_path", test_path, path
                if len(test_path) > len(path):
                    return test_path
        return path


print
StepsConstruct().construct([".#...", ".#.#.", ".#.#.", ".#.#.", "...#."], 16)
