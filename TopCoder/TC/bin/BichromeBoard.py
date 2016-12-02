class BichromeBoard:
    def ableToDraw(self, board):
        color1 = 'W'
        for r, row in enumerate(board):
            if 'W' in row:
                color1 = 'W' if (r + board[r].find("W")) % 2 == 0 else 'B'
                break
            if "B" in row:
                color1 = 'B' if (r + board[r].find("B")) % 2 == 0 else 'W'
                break
        color2 = 'W' if color1 == 'B'else'B'
        print(color1, color2)
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell != "?":
                    if (r + c) % 2 == 0 and cell != color1:
                        return "Impossible"
                    if (r + c) % 2 != 0 and cell != color2:
                        return "Impossible"
        return "Possible"


print(BichromeBoard().ableToDraw(["W?W", "??B", "???"]))
