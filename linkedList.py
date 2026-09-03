class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def get(self, index):
        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current.value
            current = current.next
            i += 1
        return -1

    def remove_front(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1

    def free_collection(self):
        self.head = None
        self.size = 0