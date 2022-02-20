class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Deque:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, value):
        element = Node(value)
        self.len += 1
        if self.head is None:
            element.previous = element
            element.next = element
            self.head = element
            return
        self.head.previous.next = element
        element.previous = self.head.previous
        self.head.previous = element
        element.next = self.head
        self.head = element

    def pop(self):
        if self.head is None:
            return None
        self.len -= 1
        element = self.head
        if self.len == 0:
            element.previous = None
            element.next = None
            self.head = None
            return element
        head = element.next
        head.previous = element.previous
        element.previous.next = head
        self.head = head
        element.previous = None
        element.next = None
        return element

    def shiftleft(self):
        if self.len != 0:
            self.head = self.head.next

    def shiftright(self):
        if self.len != 0:
            self.head = self.head.previous

    def repr(self):
        current = self.head
        for _ in range(self.len):
            yield current.value
            current = current.next

    def length(self):
        return self.len

