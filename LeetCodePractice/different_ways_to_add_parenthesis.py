import operator


class Solution:
    memoize = {}
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

    def diffWaysToCompute(self, input):
        if input.isdigit() or (input[0] == '-' and input[1:].isdigit()):
            return [int(input)]
        if input in self.memoize:
            return self.memoize[input]

        values = []
        i = 1
        while i < len(input) - 1:
            if input[i] in self.operations and input[i - 1] not in self.operations:
                op = input[i]
                values1 = self.diffWaysToCompute(input[:i])
                self.memoize[input[:i]] = values1
                values2 = self.diffWaysToCompute(input[i + 1:])
                self.memoize[input[i + 1:]] = values2

                for val1 in values1:
                    for val2 in values2:
                        values.append(self.operations[op](val1, val2))
            i += 1

        return values

    # def diffWaysToCompute(self, input):
    #     if input.isdigit() or (input[0] == '-' and input[1:].isdigit()):
    #         return [int(input)]
    #
    #     if input in self.memoize:
    #         return self.memoize[input]
    #
    #     ans = []
    #     i = 0
    #     prev_y = ''
    #     prev_s = 0
    #     while i < len(input):
    #         x = y = ''
    #         s = i
    #         while input[i] not in self.operations:
    #             x += input[i]
    #             i += 1
    #         if x == '':
    #             x = prev_y
    #             s = prev_s
    #         op = input[i]
    #         i += 1
    #         prev_s = i
    #         while i < len(input) and input[i] not in self.operations:
    #             y += input[i]
    #             i += 1
    #         print(input)
    #         print("*", x, op, y, "*")
    #         a = self.operations[op](int(x), int(y))
    #         self.memoize[input[s:i]] = [a]
    #         ans.extend(self.diffWaysToCompute(input[:s] + str(a) + input[i:]))
    #         prev_y = y
    #     return sorted(set(ans))


print(Solution().diffWaysToCompute("3-2-1"))
print(Solution().diffWaysToCompute("5*4-3*2"))
