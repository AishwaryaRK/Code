class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    p1 = p.val
    q1 = q.val
    if root.left == None and root.right == None:
        if root.val == p1:
            return p1
        if root.val == q1:
            return q1
        return None
    node = root
    v = node.val
    v1 = None
    v2 = None
    if node.left != None:
        v1 = lowestCommonAncestor(node.left, p, q)
        if type(v1) is TreeNode:
            return v1
    if node.right != None:
        v2 = lowestCommonAncestor(node.right, p, q)
        if type(v2) is TreeNode:
            return v2
    if p1 in [v, v1, v2] and q1 in [v, v1, v2]:
        return node
    elif p1 in [v, v1, v2]:
        return p1
    elif q1 in [v, v1, v2]:
        return q1
    else:
        return None
