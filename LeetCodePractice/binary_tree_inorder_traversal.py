# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        ans = []
        if root == None:
            return ans
        stack = [root]
        visited = {}
        while len(stack) != 0:
            top = len(stack) - 1
            n = stack[top]
            if n in visited:
                ans.append(n.val)
                stack.pop()
                if n.right != None:
                    stack.append(n.right)
            elif n.left == None:
                ans.append(n.val)
                visited[n] = 1
                stack.pop()
                if n.right != None:
                    stack.append(n.right)
            elif n.left != None:
                stack.append(n.left)
                visited[n] = 1
        return ans
