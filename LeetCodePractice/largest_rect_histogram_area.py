def largestRectangleArea(A):
    if len(A) == 0:
        return 0
    stack = [(0, A[0])]
    area = 0
    for i in range(1, len(A)):
        top = stack[-1]
        if top != () and A[i] < top[1]:
            node = ()
            while top != () and A[i] < top[1]:
                node = stack.pop()
                if len(stack) > 0:
                    top = stack[-1]
                else:
                    top = ()
            if node != ():
                ar = (i - node[0]) * node[1]
                if ar > area:
                    area = ar
        stack.append((i, A[i]))

    if len(stack) != 0:
        i = len(A)
        while len(stack) != 0:
            node = stack.pop()
            ar = (i - node[0]) * node[1]
            if ar > area:
                area = ar

    return area


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(largestRectangleArea([2, 6]))
