class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def pushleft(self, value):
        element = Node(value)
        element.next = self.head
        if self.head is not None:
            self.head.previous = element
        self.head = element
        if self.len == 0:
            self.tail = element
        self.len += 1

    def pushright(self, value):
        element = Node(value)
        element.previous = self.tail
        if self.tail is not None:
            self.tail.next = element
        self.tail = element
        if self.len == 0:
            self.head = element
        self.len += 1

    def popleft(self):
        if self.head is None:
            return None
        element = self.head
        self.len -= 1
        if element.next is None:
            self.head = None
            self.tail = None
            return element
        element.next.previous = None
        self.head = element.next
        return element

    def popright(self):
        if self.tail is None:
            return None
        element = self.tail
        self.len -= 1
        if element.previous is None:
            self.head = None
            self.tail = None
            return element
        element.previous.next = None
        self.tail = element.previous
        return element

    def length(self):
        return self.len
