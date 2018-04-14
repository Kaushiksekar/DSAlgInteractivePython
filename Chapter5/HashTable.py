"""This module consists of only one class which is hash table."""

class HashTable:
    """HashTable class is similar to the dictionary implementation in Python
    where the key is hashed to get a position and value is stored based on that
    position."""
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        """This method returns a hash value based on key"""
        return key % self.size

    def rehash(self, old_hash):
        """This method returns a new hash value based on old hash value"""
        return (old_hash + 1) % self.size

    def put(self, key, data):
        """The item puts key and value based on hash value calculated"""
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value)
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        """This method returns the value for a given key"""
        start_slot = self.hash_function(key)

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not stop and not found:
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

    def __str__(self):
        string = ""
        for position in range(self.size):
            string += str(self.slots[position]) + " - " + str(self.data[position]) + "\n"
        return string
