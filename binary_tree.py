from queue import Queue
from binary_tree_printer import BinaryTreePrinter

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            nodes = Queue()
            nodes.enque(self.root)

            while True:
                checking_node = nodes.deque()
                if checking_node.left is None:
                    checking_node.left = TreeNode(value)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(value)
                    return
                else:
                    nodes.enque(checking_node.left)
                    nodes.enque(checking_node.right)
