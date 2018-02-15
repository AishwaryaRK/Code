class Cross:
    def exist(self, board):
        r = len(board)
        c = len(board[0])
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if board[i][j] == board[i - 1][j] == board[i + 1][j] == board[i][j - 1] == board[i][j + 1] == "#":
                    return "Exists"
        return "Does not exist"


print(Cross().exist([".##", "###", "##."]))
