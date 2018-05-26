def root_to_leaf_path_sums(tree):
    stack = []
    stack.append((0, str(tree[0])))
    sum = 0
    while len(stack) != 0:
        i, s = stack.pop()
        li = 2 * i + 1
        ri = li + 1
        is_leaf = True
        if li < len(tree) and tree[li] != None:
            stack.append((li, s + str(tree[li])))
            is_leaf = False
        if ri < len(tree) and tree[ri] != None:
            stack.append((ri, s + str(tree[ri])))
            is_leaf = False
        if is_leaf:
            sum += int(s)
    return sum


tree = [6, 3, 5, 2, 5, None, 4, None, None, 7, 4]
print(root_to_leaf_path_sums(tree))
