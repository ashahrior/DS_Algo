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


    def __find_min(self, node):
        return node if node.left is None else self.__find_min(node.left)
    
    def __delete_value(self, node:TreeNode, value):
        if node is None:
            return node
        elif value < node.value:
            node.left = self.__delete_value(node.left, value)
        elif value > node.value:
            node.right = self.__delete_value(node.right, value)
        else:
            # case 1: no child
            if node.left is None and node.right is None:
                del node
                node = None
            # case 2: 1 children
            elif node.left is None:
                temp = node
                node = node.right
                del temp
            elif node.right is None:
                temp = node
                node = node.left
                del temp
            # case 3: 2 children
            else:
                temp = self.__find_min(node.right)
                node.value = temp.value
                node.right = self.__delete_value(node.right, temp.value)
        return node

    def delete(self, value):
        if self.root is None:
            return False
        else:
            self.__delete_value(self.root, value)


    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)

    def getNodeData(self,node:TreeNode):
        print('Node value: ', node.value)
        left = None if node.left is None else node.left.value
        print(f'Node left: [{left}]')
        right = None if node.right is None else node.right.value
        print(f'Node right: [{right}]')


    def __pre_order(self, node):
        if node is None:
            return
        print(node.value)
        self.__pre_order(node.left)
        self.__pre_order(node.right)

    def pre_order(self):
        self.__pre_order(self.root)
        print()
        return


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


    def __post_order(self, node):
        if node is None:
            return
        self.__pre_order(node.left)
        self.__pre_order(node.right)
        print(node.value)

    def post_order(self):
        self.__post_order(self.root)
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


    def __isBSTutil(self, root, minVal, maxVal):
        if root is None:
            return True
        # too many repetitive recursion calls
        # if isSubTreeLesser(root.left, root.value) and \
            # isSubTreeGreater(root.right, root.value) and \
            # isBST(root.left) and isBST(root.right):
            #     return True
        if root.value > minVal and root.value < maxVal \
                and self.__isBSTutil(root.left, minVal, root.value) \
                and self.__isBSTutil(root.right, root.value, maxVal):
            return True
        return False

    def isBST(self):
        return self.__isBSTutil(self.root,-1000,1000)

    def __getHeight(self,root):
        if root is None:
            return 0
        return max(self.__getHeight(root.left), self.__getHeight(root.right))+1

    def getHeight(self):
        return self.__getHeight(self.root)
    

    def __isBalanced(self,root: TreeNode):
        if root is None:
            return True

        left_height = self.__getHeight(root.left)
        right_height = self.__getHeight(root.right)

        if abs(left_height-right_height) <= 1 and self.__isBalanced(root.left) is True and self.__isBalanced(root.right) is True:
            return True

        return False

    def isBalanced(self):
        return self.__isBalanced(self.root)


    def __buildTree(self,nodes,start, end):
        if start > end:
            return None
        mid = (start+end)//2
        node = nodes[mid]
        # self.getNodeData(node)
        # print()
        node.left = self.__buildTree(nodes, start, mid-1)
        node.right = self.__buildTree(nodes, mid+1, end)
        return node

    def __storeBSTNodes(self,root,nodes):
        if root is None:
            return
        self.__storeBSTNodes(root.left, nodes)
        nodes.append(root)
        self.__storeBSTNodes(root.right, nodes)

    def __makeBalance(self, root:TreeNode):
        nodes = []
        self.__storeBSTNodes(root,nodes)
        #print(nodes)
        return self.__buildTree(nodes,0,len(nodes)-1)

    def makeBalance(self):
        if self.isBalanced():
            return "Already Balanced"
        return self.__makeBalance(self.root)
        



def isSubTreeLesser(root, val):
    if root is None:
        return True
    if root.value <= val and \
        isSubTreeLesser(root.left, val) and \
        isSubTreeLesser(root.right, val):
        return True
    return False

def isSubTreeGreater(root, val):
    if root is None:
        return True
    if root.value > val and \
            isSubTreeGreater(root.left, val) and \
            isSubTreeGreater(root.right, val):
        return True
    return False

def isBSTutil(root, minVal, maxVal):
    if root is None:
        return True
    # too many repetitive recursion calls
    # if isSubTreeLesser(root.left, root.value) and \
    # isSubTreeGreater(root.right, root.value) and \
    # isBST(root.left) and isBST(root.right):
    #     return True
    
    if root.value > minVal and root.value < maxVal \
        and isBSTutil(root.left, minVal, root.value) \
        and isBSTutil(root.right, root.value, maxVal):
        return True

    return False


def checkBalance(root):
    # simple dfs solution
    def depth(root):
        if not root:
            return 0
        l = depth(root.left)
        r = depth(root.right)
        if abs(l-r)>1:
            return float('inf')
        return max(l,r)+1
    return depth(root)!=float('inf')


if __name__ == "__main__":    
    tree = BinarySearchTree()

    # s = [random.randint(1, 100) for x in range(1, 10)]
    s = [12, 5, 15, 3, 7, 13, 17, 1, 9, 14, 20, 8, 11, 18]
    for x in s:
        tree.insert(x)
    print(tree)
    #tree.in_order()
    #print_tree(tree.root,0)
    # check = random.randint(1, 100)
    # print('Checking for %d - %s'%(check,tree.contains(check)))
    tree.delete(20)
    print(tree)
    # print(isBSTutil(tree.root, -1000, 1000))
    # tree.insert(10)
    # tree.root.left = TreeNode(8)
    # tree.root.left.left = TreeNode(7)
    # tree.root.left.left.left = TreeNode(6)
    # tree.root.left.left.left.left = TreeNode(5)
    # print(tree)
    print(checkBalance(tree.root))
    print('Balanced? : ', tree.isBalanced())
    print('BST? : ', tree.isBST())
    print(tree.getHeight())
    tree.makeBalance()
    print('Balanced? : ', tree.isBalanced())
    print(tree)
