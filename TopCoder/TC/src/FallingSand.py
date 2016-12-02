from pprint import pprint


class FallingSand:
    def simulate(self, board):
        new_board = [list(row) for row in board]
        while board != new_board:
            board = [list(row) for row in new_board]
            for row in range(0, len(board) - 1):
                for col, cel in enumerate(board[row]):
                    if board[row][col] == 'o' and board[row + 1][col] == '.':
                        new_board[row][col] = '.'
                        new_board[row + 1][col] = 'o'
        final_board=[]
        for row in new_board:
            str=""
            for cell in row:
                str+=cell
            final_board.append(str)
        return final_board

pprint(FallingSand().simulate(["..o..o..o..o..o..o..o..o..o..o..o",
                               "o..o..o..o..o..o..o..o..o..o..o..",
                               ".o..o..o..o..o..o..o..o..o..o..o.",
                               "...xxx...xxx...xxxxxxxxx...xxx...",
                               "...xxx...xxx...xxxxxxxxx...xxx...",
                               "...xxx...xxx......xxx......xxx...",
                               "...xxxxxxxxx......xxx......xxx...",
                               "...xxxxxxxxx......xxx......xxx...",
                               "...xxxxxxxxx......xxx......xxx...",
                               "...xxx...xxx......xxx............",
                               "...xxx...xxx...xxxxxxxxx...xxx...",
                               "...xxx...xxx...xxxxxxxxx...xxx...",
                               "..o..o..o..o..o..o..o..o..o..o..o",
                               "o..o..o..o..o..o..o..o..o..o..o..",
                               ".o..o..o..o..o..o..o..o..o..o..o."]))
