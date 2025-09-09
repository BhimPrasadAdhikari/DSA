class Node:
    """A single node in a binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Building a short perfect tree.
root = Node(10)
root.left = Node(20)
root.right = Node(30)

        