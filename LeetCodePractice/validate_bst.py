class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


MINUS_INFINITY = "-infinity"
PLUS_INFINITY = "+infinity"


class Solution:
    def isValidBST(self, root):
        return self.is_valid_bst(root, MINUS_INFINITY, PLUS_INFINITY)

    def is_valid_bst(self, root, min, max):
        if root == None:
            return True

        m1 = min
        m2 = max
        if min == MINUS_INFINITY:
            m1 = root.val - 1
        if max == PLUS_INFINITY:
            m2 = root.val + 1

        if m1 < root.val < m2:
            return self.is_valid_bst(root.left, min, root.val) and \
                   self.is_valid_bst(root.right, root.val, max)

        return False
