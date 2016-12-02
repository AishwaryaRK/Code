def maxDifference(a):
    maxDifference = -1
    length = len(a)
    for i, n in enumerate(a):
        for j in range(i + 1, length):
            if a[j] > a[i] and a[j] - a[i] >= maxDifference:
                maxDifference = a[j] - a[i]
    return maxDifference


def braces(values):
    opening_braces = ['{', '(', '[']
    closing_braces = ['}', ')', ']']
    brace_pairs = {'{': '}', '(': ')', '[': ']'}
    output = []
    for value in values:
        stack = []
        flag = True
        for brace in value:
            if brace in opening_braces:
                stack.append(brace)
            elif brace in closing_braces:
                if len(stack) == 0:
                    output.append('NO')
                    flag = False
                    break
                popped_brace = stack.pop()
                if brace_pairs[popped_brace] != brace:
                    output.append('NO')
                    flag = False
                    break
        if len(stack) == 0 and flag:
            output.append('YES')
        elif flag:
            output.append('NO')
    return output


from collections import Counter


def rearrangeWord(word):
    letter_freq = Counter(list(word))
    if len(letter_freq) == 1:
        return 'no answer'
    greater_letter = max(letter_freq)
    for j, letter in enumerate(word):
        if greater_letter == letter:
            letter_freq.pop(greater_letter)
            if len(letter_freq)==0:
                return word
            greater_letter = max(letter_freq)
        else:
            break
    print(greater_letter)
    index = max([i for i, c in enumerate(word) if c == greater_letter])
    output = word[0:index - 1] + greater_letter + word[index - 1] + word[index + 1:]
    return output


print(rearrangeWord('hefg'))
