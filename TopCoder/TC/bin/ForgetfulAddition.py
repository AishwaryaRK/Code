class ForgetfulAddition:
    def minNumber(self, expression):
        ans = []
        for i in range(0, len(expression) - 1):
            ans.append(int(expression[:i + 1]) + int(expression[i + 1:]))
        return min(ans)


print(ForgetfulAddition().minNumber("1289"))
