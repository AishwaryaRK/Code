import re
import math


class CollectingRiders:
    def minimalMoves(self, board):
        pivot = None
        for i, row in enumerate(board):
            m = re.search("\d", row)
            if m != None:
                pivot = (i, m.start())
                break

        if pivot == None:
            return 0

        cnt = 0
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if pivot != (i, j) and board[i][j] != '.':
                    step_horse = int(board[i][j])
                    positions_covered = []
                    n = self.can_reach_pivot_in_n_steps(i, j, step_horse, pivot, board, positions_covered)
                    if n == -1:
                        return -1
                    cnt += n

        return cnt

    def can_reach_pivot_in_n_steps(self, i, j, step_horse, pivot, board, positions_covered):
        if pivot == (i, j):
            return 0

        if (i, j) in positions_covered:
            return -1

        positions_covered.append((i, j))
        n = []
        r, c = len(board), len(board[0])

        if i - 2 >= 0 and j + 1 < c:
            n1 = self.can_reach_pivot_in_n_steps(i - 2, j + 1, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))
        if i - 2 >= 0 and j - 1 >= 0:
            n1 = self.can_reach_pivot_in_n_steps(i - 2, j - 1, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))
        if i + 2 < r and j + 1 < c:
            n1 = self.can_reach_pivot_in_n_steps(i + 2, j + 1, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))
        if i + 2 < r and j - 1 >= 0:
            n1 = self.can_reach_pivot_in_n_steps(i + 2, j - 1, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))

        if i - 1 >= 0 and j + 2 < c:
            n1 = self.can_reach_pivot_in_n_steps(i - 1, j + 2, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))
        if i - 1 >= 0 and j - 2 >= 0:
            n1 = self.can_reach_pivot_in_n_steps(i - 1, j - 2, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))
        if i + 1 < r and j + 2 < c:
            n1 = self.can_reach_pivot_in_n_steps(i + 1, j + 2, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))
        if i + 1 < r and j - 2 >= 0:
            n1 = self.can_reach_pivot_in_n_steps(i + 1, j - 2, step_horse, pivot, board, positions_covered[:])
            if n1 != -1:
                n.append(n1 + len(positions_covered))

        print(i, j, positions_covered, n)
        return -1 if len(n) == 0 else math.ceil(min(n) / step_horse)


board = ["........",
         ".1......",
         "........",
         "....3...",
         "........",
         "........",
         ".7......",
         "........"]

print(CollectingRiders().minimalMoves(board))
