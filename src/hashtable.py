# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"{self.key}, {self.value}"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_value = 5381
    # Bit-shift and sum value for each character
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # if self.count / self.capacity >= .7:
        #     self.resize()

        pair = self.storage[index]
        if pair is not None:
            
            prev_node = None
            while pair is not None:
                if pair.key == key:
                    pair.value = value
                    return
                prev_node = pair
                pair = pair.next

            self.count += 1
            prev_node.next = LinkedPair(key, value)
        else:
            self.count += 1
            self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None and self.storage[index].key == key:
            self.count -= 1
            # if self.count / self.capacity <= .2:
            #     self.resize()            
            self.storage[index] = None

        elif self.storage[index] is not None:
            current = self.storage[index]
            prev_node = None

            while current.key != key and current.next is not None:
                prev_node = current
                current = current.next

            if current.key == key:
                self.count -= 1
                # if self.count / self.capacity <= .2:
                #     self.resize()                 
                prev_node.next = current.next
                current = None
            else:
                print("Key was not found")

        else:
            print("Warning! Key does not exist")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    return current.value
                else:
                    current = current.next
        else:
            print("Warning! Key does not exist")
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        if self.count != 0 and self.count / self.capacity <= .2:
            self.capacity /= 2
        else:
            self.capacity *= 2

        temp_hash_table = [None] * self.capacity
        clone = self.storage
        self.storage = temp_hash_table

        for pair in clone:
            if pair is not None:
                current = pair
                while current is not None:
                    self.insert(current.key, current.value)
                    current = current.next





if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
