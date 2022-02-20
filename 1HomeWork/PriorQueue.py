class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.priority = None


class PriorQueue:
    def __init__(self):
        self.head = None
        self.lastlow = None
        self.len = 0

    def enqueue(self, element):
        self.len += 1
        if self.head is None:
            self.head = element
            if element.priority == 0:
                self.lastlow = element
            return
        if element.priority == 1 and self.lastlow is not None:
            element.next = self.lastlow.next
            self.lastlow.next = element
            return
        element.next = self.head
        self.head = element

    def dequeue(self):
        if self.len == 0:
            return None
        if self.len == 1:
            element = self.head
            self.lastlow = None
            self.head = None
            self.len = 0
            return element
        self.len -= 1
        current = self.head
        while current.next.next is not None:
            current = current.next
        element = current.next
        current.next = None
        if element.priority == 0:
            self.lastlow = current
        return element

    def length(self):
        return self.len
