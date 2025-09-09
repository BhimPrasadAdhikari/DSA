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
    """Traverse the tree in left sub-tree -> root -> right sub-tree"""
    if root_node is None:
        return
    inorder(root_node.left)
    print(root_node.data)
    inorder(root_node.right)
    
def preorder(root_node):
    """Traverse the tree in root -> left sub-tree -> right sub-tree flow"""
    if root_node is None:
        return
    print(root_node.data)
    preorder(root_node.left)
    preorder(root_node.right)
    
def postorder(root_node):
    """Traverse the tree in left sub-tree -> right sub-tree -> root flow"""
    if root_node is None:
        return
    preorder(root_node.left)
    preorder(root_node.right)
    print(root_node.data)
    
    

inorder(root)    
preorder(root)
postorder(root)