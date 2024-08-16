"""
Implementation of circular double linked list.
"""
class Node:
    """
    A class representing a node in a circular doubly linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node in the list.
        prev: Reference to the previous node in the list.
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularLinkedList:
    """
    A class implementing a circular doubly linked list data structure.

    Attributes:
        head: Reference to the first node in the list.
        tail: Reference to the last node in the list.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_element(self, value, index):
        """
        Insert a new element at the specified index in the circular list.

        Args:
            value: The value to be inserted.
            index (int): The position at which to insert the new element.

        Returns:
            str: "Not possible" if the insertion is not possible at the given index.
        """
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            self.head.next = self.head.prev = self.tail
            return
        
        if index == 0:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
            return

        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next
            if current_node == self.head:
                return "Not possible"

        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next.prev = new_node
        current_node.next = new_node
        
        if new_node.next == self.head:
            self.tail = new_node

    def remove_element(self, index):
        """
        Remove an element at the specified index from the circular list.

        Args:
            index (int): The position of the element to be removed.

        Returns:
            str: "No elements remaining" if the list is empty.
                 "Not possible" if the removal is not possible at the given index.
        """
        if not self.head:
            return "No elements remaining"
        
        if self.head == self.tail:
            self.head = self.tail = None
            return

        if index == 0:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            del temp
            return

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
            if current_node == self.head:
                return "Not possible"

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        
        if current_node == self.tail:
            self.tail = current_node.prev
        
        del current_node

    def traverse_forward(self):
        """
        Traverse the circular list from head to tail and return a string representation.

        Returns:
            str: A string representation of the list elements connected by " <-> ".
        """
        if not self.head:
            return ""
        result = []
        current_node = self.head
        while True:
            result.append(str(current_node.value))
            current_node = current_node.next
            if current_node == self.head:
                break
        return " <-> ".join(result)

    def traverse_backward(self):
        """
        Traverse the circular list from tail to head and return a string representation.

        Returns:
            str: A string representation of the list elements connected by " <-> ".
        """
        if not self.tail:
            return ""
        result = []
        current_node = self.tail
        while True:
            result.append(str(current_node.value))
            current_node = current_node.prev
            if current_node == self.tail:
                break
        return " <-> ".join(result)

if __name__ == "__main__":
    double_ll = CircularLinkedList()
    double_ll.insert_element(1, 0)
    double_ll.insert_element(2, 1)
    double_ll.insert_element(3, 2)
    double_ll.insert_element(4, 3)
    print(double_ll.traverse_forward())
    print(double_ll.traverse_backward())
    double_ll.insert_element("Hello", 4)
    print(double_ll.traverse_forward())

    double_ll.remove_element(4)
    print(double_ll.traverse_forward())
    double_ll.remove_element(0)
    print(double_ll.traverse_forward())
    print(double_ll.traverse_backward())