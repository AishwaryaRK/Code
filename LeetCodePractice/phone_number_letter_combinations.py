def letterCombinations(digits):
    a = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}

    stack = []
    for i, d in enumerate(digits):
        if i == 0:
            for c in a[d]:
                stack.append(c)
            continue
        temp = []
        for c in a[d]:
            for s in stack:
                temp.append(s+c)

        stack = temp
    return stack

print(letterCombinations("23"))