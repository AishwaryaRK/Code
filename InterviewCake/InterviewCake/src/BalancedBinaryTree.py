class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def __str__(self):
        return str(self.value) + "," + str(self.left) + "," + str(self.right)


def is_binary_tree_superbalanced(root):
    current_level_nodes = [root]
    current_level = 0
    leaf_node_heights = []
    while len(current_level_nodes) > 0:
        next_level_nodes = []
        for node in current_level_nodes:
            if node.left == None and node.right == None:
                leaf_node_heights.append(current_level)
            else:
                if node.left != None:
                    next_level_nodes.append(node.left)
                if node.right != None:
                    next_level_nodes.append(node.right)
        current_level += 1
        current_level_nodes = next_level_nodes
    leaf_node_heights = set(leaf_node_heights)
    return max(leaf_node_heights) - min(leaf_node_heights) <= 1


root = BinaryTreeNode(1)
lroot=root.insert_left(2)
rroot=root.insert_right(3)
llroot=lroot.insert_left(4)
rrroot=rroot.insert_left(5)
rroot.insert_right(9).insert_right(10)
llroot.insert_left(6)
print(is_binary_tree_superbalanced(root))
