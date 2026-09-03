TABLE_SIZE = 10007

class Entry:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.buckets = [None] * TABLE_SIZE

    def _hash(self, value):
        return value % TABLE_SIZE

    def hash_insert(self, value):
        index = self._hash(value)
        new_entry = Entry(value)
        new_entry.next = self.buckets[index]
        self.buckets[index] = new_entry

    def hash_contains(self, value):
        index = self._hash(value)
        current = self.buckets[index]
        while current is not None:
            if current.value == value:
                return 1
            current = current.next
        return 0

    def hash_free(self):
        self.buckets = [None] * TABLE_SIZE