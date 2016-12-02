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
        return str(self.value)


def second_largest_item_in_bst(root):
    second_largest_item_in_bst = None
    current_node = root
    while current_node.right != None:
        second_largest_item_in_bst = current_node
        current_node = current_node.right
    return second_largest_item_in_bst


root = BinaryTreeNode(50)
lroot = root.insert_left(30)
rroot = root.insert_right(80)
llroot = lroot.insert_left(20)
rrroot = rroot.insert_left(60)
rroot.insert_right(90).insert_right(100).insert_right(122)
llroot.insert_left(10)
print(second_largest_item_in_bst(root))
