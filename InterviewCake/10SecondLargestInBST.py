def second_largest_item_in_bst(root):
    second_largest_item_in_bst = None
    current_node = root
    while current_node != None:
        if current_node.right_child.right_child == None and current_node.right_child.left_child == None:
            return current_node
        if current_node.right_child == None and current_node.left_child != None:
            current_node = current_node.left_child
        current_node = current_node.right_child
