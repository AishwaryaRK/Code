from collections import Counter


def get_possible_words(dictionary, board):
    m = len(board)
    n = len(board[0])

    sequences = []
    for i in range(0, m):
        for j in range(0, n):
            sequence = ""
            sequence += board[i][j]
            if j > 0:
                sequence += board[i][j - 1]
            if j < n - 1:
                sequence += board[i][j + 1]
            if i > 0:
                sequence += board[i - 1][j]
            if i > 0 and j > 0:
                sequence += board[i - 1][j - 1]
            if i > 0 and j < n - 1:
                sequence += board[i - 1][j + 1]
            if i < m - 1:
                sequence += board[i + 1][j]
            if i < m - 1 and j > 0:
                sequence += board[i + 1][j - 1]
            if i < m - 1 and j < n - 1:
                sequence += board[i + 1][j + 1]
            sequences.append(sequence)

    possible_words = []
    for sequence in sequences:
        f1 = Counter(sequence)
        for word in dictionary:
            if len(word) <= len(sequence):
                f2 = Counter(word)
                flag = True
                for k, v in f2.items():
                    if (k not in f1) or (k in f1 and f1[k] < v):
                        flag = False
                        break
                if flag and word not in possible_words:
                    possible_words.append(word)

    possible_words = sorted(possible_words)
    return possible_words if len(possible_words) > 0 else ["-1"]


t = int(input())
for i in range(0, t):
    input()
    dictionary = list(map(str.strip, input().split(' ')))
    n, m = map(int, input().split(' '))
    s = input().split(' ')
    board = []
    for j in range(0, m):
        row = []
        for k in range(0, n):
            row.append(s[j * n + k])
        board.append(row)
    print(*get_possible_words(dictionary, board))
