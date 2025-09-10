class Node:
    """A single node in a binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
    def _insert_recursive(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(data, current_node.right)

# Building a short perfect tree.
# A perfect tree has 2^h leaf nodes and 2^(h + 1) -1 total nodes.
my_tree = BinaryTree()

datas = [10,20,30,40,50]
for data in datas:
    my_tree.insert(data)

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
    
    

inorder(my_tree.root)    
preorder(my_tree.root)
postorder(my_tree.root)