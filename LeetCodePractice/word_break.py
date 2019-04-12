def wordBreak(s, wordDict):
    n = len(s)
    mat = [[0] * n for i in range(0, n)]

    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            a = s[j:j + i]
            if a in wordDict:
                mat[j][j + i - 1] = 1
            else:
                for k in range(j + 1, j + i):
                    # x = s[j:k]
                    # y = s[k:j + i]
                    if mat[j][k - 1] == 1 and mat[k][j + i - 1] == 1:
                        mat[j][j + i - 1] = 1
                        break

    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(mat)
    return mat[0][-1] == 1


# print(wordBreak("catand", ["cats", "dog", "sand", "and", "cat"]))
print(wordBreak("applepenapple", ["apple", "pen"]))
