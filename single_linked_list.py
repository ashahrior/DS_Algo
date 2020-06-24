class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        self.tail.next = node
        self.tail = node
        self.size += 1
        return

    '''def __remove__node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1
        return'''

    '''def remove(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.__remove__node(node)
            node = node.next
        return'''

    '''def pop_front(self):
        if self.head is not None:
            self.__remove__node(self.head)'''

    '''def pop_back(self):
        if self.tail is not None:
            self.__remove__node(self.tail)
        return'''

    def search(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.value)
            node = node.next
        return str(', '.join(str(value) for value in vals))


if __name__ == "__main__":
    ml = SingleLinkedList()
    ml.add(1)
    ml.add(4)
    ml.add(3)
    ml.add(0)
    ml.add(1)
    ml.add(3)
    ml.add(45)
    print(ml)
