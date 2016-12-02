def is_balanced(root):
    depths = []
    stack = [(root, 0)]
    while len(stack) > 0:
        node, depth = stack.pop()
        if node.left_child == None and node.right_child == None:
            if depth not in depths:
                depths.append(depth)
            if len(depths) > 2 or abs(depths[0] - depths[1] > 1):
                return False
        else:
            if node.left_child != None:
                stack.append(node.left_child, depth + 1)
            if node.right_child != None:
                stack.append(node.right_child, depth + 1)
        return True
