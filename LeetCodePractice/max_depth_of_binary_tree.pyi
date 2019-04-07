class Solution:
    #[3,9,20,null,null,15,7]

    #    3
    #  / \
    # 9  20
    #   /  \
    #  15   7

    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left, root.right))
