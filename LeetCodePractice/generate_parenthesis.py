# n=3
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def generateParenthesis(n):
    if n == 0:
        return []
    sub_ans = ['()']
    for i in range(2, n + 1):
        ans = []
        for j, pattern in enumerate(sub_ans):
            for k, c in enumerate(pattern):
                if c == '(':
                    s = pattern[:k + 1] + "()" + pattern[k + 1:]
                    ans.append(s)
            if j == len(sub_ans) - 1:
                s = pattern + '()'
                ans.append(s)
        sub_ans = set(ans)
    return sub_ans


print(len(generateParenthesis(4)))
