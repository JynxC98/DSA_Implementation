"""
Implementation of HashMap on Python without dictionary.
"""

class HashMap:
    """
    A simple HashMap implementation using Python.

    This class provides basic HashMap functionality including adding key-value pairs,
    retrieving values by key, deleting key-value pairs, and printing the contents.

    Attributes:
        size (int): The number of buckets in the HashMap.
        map (list): A list of lists, where each inner list represents a bucket.
    """

    def __init__(self, size=100):
        """
        Initialize the HashMap.

        Args:
            size (int): The number of buckets in the HashMap. Defaults to 100.
        """
        self.size = size
        self.map = [[] for _ in range(self.size)]
    
    def _get_hash(self, key):
        """
        Compute the hash value for a given key.

        Args:
            key: The key to be hashed.

        Returns:
            int: The computed hash value.
        """
        return hash(key) % self.size
    
    def add(self, key, value):
        """
        Add a key-value pair to the HashMap.

        If the key already exists, its value will be updated.

        Args:
            key: The key to be added.
            value: The value associated with the key.

        Returns:
            bool: True if the operation was successful.
        """
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
    
    def get(self, key):
        """
        Retrieve the value associated with a given key.

        Args:
            key: The key whose value is to be retrieved.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        """
        Delete a key-value pair from the HashMap.

        Args:
            key: The key of the pair to be deleted.

        Returns:
            bool: True if the key was found and deleted, False otherwise.
        """
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
    
    def print(self):
        """
        Print all the key-value pairs in the HashMap.
        """
        for item in self.map:
            if item:
                print(str(item))

if __name__ == "__main__":
    
    h = HashMap()
    h.add('Bob', '567-8888')
    h.add('Ming', '293-6753')
    h.add('Ming', '333-8233')
    h.add('Ankit', '293-8625')
    h.add('Aditya', '852-6551')
    h.add('Alicia', '632-4123')
    h.add('Mike', '567-2188')
    h.print()
    print(h.get('Ming'))
    h.delete('Bob')
    h.print()