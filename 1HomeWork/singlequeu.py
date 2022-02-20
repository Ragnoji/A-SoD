class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self, value):
        element = Node(value)
        element.next = self.head
        self.head = element
        if self.len == 0:
            self.tail = self.head
        self.len += 1

    def dequeue(self):
        if self.len == 0:
            return None
        if self.len == 1:
            element = self.head
            self.head = None
            self.tail = None
            return element
        self.len -= 1
        current = self.head
        while current.next.next is not None:
            current = current.next
        element = current.next
        current.next = None
        self.tail = current
        return element

    def check(self):
        return self.tail.value

    def length(self):
        return self.len
