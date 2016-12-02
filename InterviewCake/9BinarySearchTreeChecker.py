def is_bst(root):
    stack = []
    node = root
    last = None
    while len(stack) > 0:
        if node != None:
            stack.append(node)
            node = node.left_child
        else:
            node = stack.pop()
            if last != None and last > node.value:
                return False
            else:
                last = node.value
            node = node.right_child
    return True
