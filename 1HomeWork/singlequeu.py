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
        if self.length == 0:
            return None
        prev = self.head
        current = prev.next
        self.len -= 1
        if current is None:
            self.head = None
            self.tail = None
            return prev
        while current.next is not None:
            prev = prev.next
            current = current.next
        prev.next = None
        self.tail = prev
        return current

    def check(self):
        return self.tail.value

    def length(self):
        return self.len
