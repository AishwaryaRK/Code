class EightRooks:
    def isCorrect(self, board):
        for i in range(len(board)):
            if (board[i].count("R") !=1):
                return "Incorrect"
            s = ""
            for row in board:
                s += row[i]
            print(s)
            if (s.count("R")!=1):
                return "Incorrect"
        return "Correct"


print(EightRooks().isCorrect(
    ("R.......", "........", "..R.....", "...R....", "....R...", ".....R..", "......R.", ".......R")))
