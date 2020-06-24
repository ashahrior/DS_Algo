import random
from queue import Queue
from stack import Stack
from binary_tree_printer import BinaryTreePrinter, print_tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node is None:
            return
        if node.value == value:
            return
        elif node.value > value:
            if node.left is None:
                node.left = TreeNode(value)
                return
            self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return
            self.__insert_value(node.right, value)

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.__insert_value(self.root, value)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)

    def __in_order(self, node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.value, end=' ')
        self.__in_order(node.right)
        return

    def in_order(self):
        self.__in_order(self.root)
        print()
        return

    def contains(self, value):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            print('Checking node', node.value)
            if node.value == value:
                return True
            elif node.value < value:
                if node.right is not None:
                    nodes.push(node.right)
            else:
                if node.left is not None:
                    nodes.push(node.left)
        return False


'''
if __name__ == "__main__":    
    tree = BinarySearchTree()

    s = [random.randint(1, 100) for x in range(1, 10)]
    for x in s:
        tree.insert(x)
    print(tree)
    tree.in_order()
    #print_tree(tree.root,0)
    check = random.randint(1, 100)
    print('Checking for %d - %s'%(check,tree.contains(check)))
'''
