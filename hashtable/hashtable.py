class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # create fnv_offset_basis
        hash = 14695981039346656037
        # iterate over data
        for char in key:
        # hash = offset_basis multiplied by FNV_prime
            hash = hash * 1099511628211
        # hash = hash xor octet_of_data
            hash = hash ^ ord(char)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for char in key:
            hash = (( hash << 5) + hash) + ord(char)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # get key_index using self.hash_index(key)
        key_index = self.hash_index(key)
        ## if location has value, add to next node in linked list
        if self.storage[key_index] is not None:
            node = self.storage[key_index]
            while node.next is not None and node.key != key:
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = HashTableEntry(key, value)
                self.load = self.load + 1 
        else:
        # insert value at key_index in hashtable
            self.storage[key_index] = HashTableEntry(key, value)
            self.load = self.load + 1 

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        key_index = self.hash_index(key)
        key_to_remove = self.storage[key_index]
        if key_to_remove is None:
            return 0
        if (key_to_remove.key == key):
            if key_to_remove.next is not None:
                self.storage[key_index] = key_to_remove.next
            else:
                self.storage[key_index] = None
            self.load = self.load - 1
            return 1
        else:
            previous_key = key_to_remove
            key_to_remove = key_to_remove.next
            while key_to_remove.key != key:
                previous_key = key_to_remove
                key_to_remove = key_to_remove.next
            if key_to_remove.next is not None:
                previous_key.next = key_to_remove.next
            else:
                previous_key.next = None
            self.load = self.load - 1
            return 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        key_index = self.hash_index(key)
        node = self.storage[key_index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def resize_helper(self, hash_entry, new_storage):
        new_key_index = self.hash_index(hash_entry.key)
        new_hash_entry = HashTableEntry(hash_entry.key, hash_entry.value)

        new_slot = new_storage[new_key_index]
        if new_slot is not None:
            while new_slot.next is not None:
                new_slot = new_slot.next
            new_slot.next = new_hash_entry
        else:
            new_storage[new_key_index] = new_hash_entry

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        new_storage = [None] * self.capacity

        for key_index in self.storage:
            hash_entry = key_index
            while hash_entry is not None:
                self.resize_helper(hash_entry, new_storage)
                hash_entry = hash_entry.next

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
