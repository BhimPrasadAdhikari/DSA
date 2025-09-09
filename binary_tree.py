class Node:
    """A single node in a binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Building a short perfect tree.
# A perfect tree has 2^h leaf nodes and 2^(h + 1) -1 total nodes.
root = Node(10)
root.left = Node(20)
root.right = Node(30)

# Traversing the tree

# 1. Inorder traverse (left sub-tree -> root -> right sub-tree)
def inorder(root_node):
    if root_node is None:
        return
    inorder(root_node.left)
    print(root_node.data)
    inorder(root_node.right)
    
inorder(root)    