from double_linked_list import DoubleLinkedList

class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, value):
        self.__list.add(value)

    def pop(self):
        val = self.__list.pop_back()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def size(self):
        return self.__list.size

    def __len__(self):
        return self.__list.size

'''
if __name__ == "__main__":
    stk = Stack()
    stk.push(1)
    stk.push(4)
    stk.push(9)
    print(stk.size())
    stk.push(3)
    stk.push(2)
    stk.push(6)
    print(len(stk))
    print(stk.pop())
    print(len(stk))
    print(stk.peek())
    print(stk.is_empty())
    print(len(stk))
'''