class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if root == None:
            return None
        queue = [root]
        ans = []
        while len(queue) != 0:
            queue.append(None)
            l = []
            n = queue.pop(0)
            while n != None:
                l.append(n.val)
                if n.left != None:
                    queue.append(n.left)
                if n.right != None:
                    queue.append(n.right)
                n = queue.pop(0)
            ans.append(l)

        return ans
