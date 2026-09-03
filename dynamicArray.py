class DynamicArray:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.data = [None] * self.capacity

    def _grow(self):
        self.capacity = self.capacity*2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def insert_back(self, value):
        if self.size == self.capacity:
            self._grow()
        self.data[self.size] = value
        self.size += 1

    def insert_front(self, value):
        if self.size == self.capacity:
            self._grow()
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]
        self.data[0] = value
        self.size += 1

    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def get(self, index):
        return self.data[index]

    def remove_front(self):
        if self.size == 0:
            return
        for i in range(self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def free_collection(self):
        self.data = None
        self.size = 0
        self.capacity = 0