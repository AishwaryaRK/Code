class BearPasswordAny:
    def findPassword(self, x):
        password = "a" * len(x) * x[-1]
        x = x[:-1]
        length = len(x)
        # print(x)
        for freq in reversed(x):
            cnt = self.getConstantSubstringsCount(password, length)
            print(password, cnt, freq, length)
            if cnt > freq:
                return ""
            if cnt < freq:
                for i in range(0, freq - cnt):
                    char = 'a' if password == "" or password[-1] == 'b' else 'b'
                    password = password + char * length
            length = length - 1
        return password

    def getConstantSubstringsCount(self, password, length):
        str1 = "a" * length
        str2 = "b" * length
        cnt = 0
        for i in range(0, len(password)):
            if i + length <= len(password):
                substr = password[i:i + length]
                # print(i, substr)
                if substr == str1 or substr == str2:
                    cnt = cnt + 1
        return cnt


# print("ans =", BearPasswordAny().getConstantSubstringsCount("aaa", 2))
print(BearPasswordAny().findPassword((5, 0, 0, 0, 0)))
