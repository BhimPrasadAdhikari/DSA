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
                
    def delete(self, data):
        self.root = self._delete_recursive(current_node, data)
    
    def _delete_recursive(self, current_node, data):
        if current_node is None:
            return current_node
        if current_node.data > data:
            current_node.left = self. _delete_recursive(current_node.left, data) 
        elif current_node.data < data:
            current_node.right = self._delete_recursive(current_node.right, data)
        else:
            # I found the node to be deleted
            # 1. The node is a leaf
            if current_node.left is None and current_node.right is None:
                return None
            # 2. the node has only one child
            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            # 3. The node has two childrens
            else:
                inorder_successor = _inorder_successor(current_node.right)
                current_node.data = inorder_successor.data
                current_node.right = self._delete_recursive(current_node.right, successor)

        return current_node
    def _inorder_successor(self, current_node):
        successor = current_node
        while successor.left is not None:
            successor = successor.left
        
        return successor
        
    
        
        
             
        

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

# Deletion of a node in the tree seems a bit complex
# There rises three cases when I want to delete a node
# 1. The node is a leaf then I can simply delete it.
# 2. The node is has a single child, then I can replace it with its child value and delete the child node
# 3. The node can have two childrens then I have to replace the parent node with the in-order successor and delete the in-order successor node.
