"""
Implementation of Array data structure from scratch using Python.
"""


class Array:
    """
    A class that implements a basic array data structure with homogeneous elements.

    This class provides a dynamic-size array with methods for accessing,
    modifying, and searching elements. All elements must be of the same type.

    Attributes:
        items (list): The internal list used to store array elements.
        size (int): The current number of elements in the array.
        type (type): The type of elements stored in the array.
    """

    def __init__(self, size, type_=None):
        """
        Initialize an empty Array.
        """
        self.size = size
        self.type_ = type_
        self.items = [None] * size
        self.length = 0

    def get(self, index):
        """
        Get the item at the specified index.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            The item at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < self.length:
            return self.items[index]
        raise IndexError("Array index out of range")


    def search(self, value):
        """
        Search for a value in the array.

        Args:
            value: The value to search for.

        Returns:
            int: The index of the first occurrence of the value,
                 or -1 if the value is not found.
        """
        for i in range(self.length):
            if self.items[i] == value:
                return i
        return -1
    
    def set_(self, index, value):
        """
        Replaces the value of the element at index `i` with a new value.

        Args:
            value: The new value
            index: The index to be replaced.
        """
        if 0 <= index < self.size:
            if self.type_ is None or isinstance(value, self.type_):
                self.items[index] = value
                if index >= self.length:
                    self.length = index + 1
            else:
                raise TypeError(f"Array elements must be of type {self.type_}")
        else:
            raise IndexError("Array index out of range")

    def append(self, value):
        """
        Append a value to the end of the array.

        Args:
            value: The value to append.

        Raises:
            TypeError: If the value is not of the same type as other elements.
        """
        if self.length >= self.size:
            raise MemoryError("Array is full")
        if self.type_ is None or isinstance(value, self.type_):
            self.items[self.length] = value
            self.length += 1
        else:
            raise TypeError(f"Array elements must be of type {self.type_}")

    def insert(self, index, value):
        """
        Insert a value at the specified index.

        Args:
            index (int): The index at which to insert the value.
            value: The value to insert.

        Raises:
            IndexError: If the index is out of range.
            TypeError: If the value is not of the same type as other elements.
        """

        # Base cases
  
        if self.length >= self.size:
            raise MemoryError("Array is full")
        if 0 <= index <= self.length:
            if self.type_ is None or isinstance(value, self.type_):
                for i in range(self.length, index, -1):
                    self.items[i] = self.items[i - 1]
                self.items[index] = value
                self.length += 1
            else:
                raise TypeError(f"Array elements must be of type {self.type_}")
        else:
            raise IndexError("Array index out of range")
        
    def remove(self, value):
        """
        Remove the first occurrence of a value from the array.

        Args:
            value: The value to remove.

        Raises:
            ValueError: If the value is not found in the array.

        """
        if value not in self.items:
            raise ValueError("Element not found")
        
        # Using `pop` for this method

        index = -1

        for i in range(self.length):
            if self.items[i] == value:
                index = i

        if index == -1:
            raise ValueError("Element not found")
        
        for i in range(index, self.length - 1):
            self.items[i] = self.items[i + 1]
        self.items[self.length - 1] = None
        self.length -= 1

    def __repr__(self):
        """
        Required to print the array.
        """
        return f"Array({self.items[:self.length]})"


if __name__ == "__main__":
    # Example usage
    arr = Array(5, int)
    arr.append(5) # Should be [5]
    arr.append(4) # Should be [5, 4]
    arr.append(6) # Should be [5, 4, 6]
    arr.append(4) # Should be [5, 4, 6, 4]
    arr.remove(4) # Should be [5, 6, 4]
    print(arr)

