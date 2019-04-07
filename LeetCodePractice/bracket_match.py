def bracket_match(text):
    stack = 0
    c = 0
    for b in text:
        if b == '(':
            stack += 1
        elif b == ')':
            if stack == 0:
                c += 1
            else:
                stack -= 1
    c += stack
    return c


print(bracket_match(")("))
