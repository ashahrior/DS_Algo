class Stack:
    class __Node:
        def __init__(self, data):
            self.__data = data
            self.__next = None
    
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def push(self, data):
        __node = self.__Node(data)
        if self.__head is None:
            self.__head = __node
            self.__size += 1
        else:
            __node._Node__next = self.__head
            self.__head = __node
            self.__size += 1
    
    def length(self):
        if self.__head is None:
            return 0
        return self.__size
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.__head._Node__data

    def pop(self):
        if self.isEmpty():
            return None
        __tmp = self.__head
        self.__head = self.__head._Node__next
        self.__size -= 1
        return __tmp._Node__data

    def __str__(self):
        __current = self.__head
        s = "["
        while __current:
            s += str(__current._Node__data)+","
            __current = __current._Node__next
        s += "]"
        return s

    def isEmpty(self):
        return self.__head==None


c = Stack()
print(c.isEmpty())
c.peek()
c.push(1)
c.push(10)
c.push(14)
c.push('ad')
print(c.peek())
c.push(100)
print(c.length())
c.push(45)
c.push(-4)
print(c)
print(c.length())
print(c.peek())
print(c.pop())
c.pop()
print(c)
print(c.isEmpty())
