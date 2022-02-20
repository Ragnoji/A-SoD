class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        head = Node(value)
        head.next = self.head
        self.head = head
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        element = self.head
        self.head = self.head.next
        self.length -= 1
        return element

    def peek(self):
        if self.length == 0:
            return None
        return self.head.value

    def is_empty(self):
        return self.head is None
