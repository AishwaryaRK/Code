class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    root = None

    def buildTree(self, preorder, inorder):
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        if self.root == None:
            self.root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            self.root.left = self.buildTree(preorder[1:], inorder[:i])
            self.root.right = self.buildTree(preorder[1:], inorder[i + 1:])
            return self.root
        else:
            for j, p in enumerate(preorder):
                if p in inorder:
                    temp_root = TreeNode(preorder[j])
                    i = inorder.index(preorder[j])
                    temp_root.left = self.buildTree(preorder[j + 1:], inorder[:i])
                    temp_root.right = self.buildTree(preorder[j + 1:], inorder[i+1:])
                    return temp_root


print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
