from double_linked_list import DoubleLinkedList

class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enque(self, value):
        self.__list.add(value)

    def deque(self):
        val = self.__list.pop_front()
        return val
    
    def front(self):
        return self.__list.front()

    def __len__(self):
        return self.__list.size

    def size(self):
        return self.__list.size

    def is_empty(self):
        return self.__list.size == 0

'''
if __name__ == "__main__":    
    qq = Queue()

    qq.enque(4)
    qq.enque(9)
    qq.enque(6)
    print(qq.size())
    qq.enque(1)
    qq.enque(3)
    qq.enque(0)
    print(len(qq))
    print(qq.deque())
    print(qq.front())
    print(len(qq))
    print(qq.is_empty())
'''