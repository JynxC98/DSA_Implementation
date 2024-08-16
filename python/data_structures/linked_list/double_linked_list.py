"""
Implementation of double linked list.
"""

class Node:
    """
    A class representing a node in a doubly linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node in the list.
        prev: Reference to the previous node in the list.
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    """
    A class implementing a doubly linked list data structure.

    Attributes:
        head: Reference to the first node in the list.
        tail: Reference to the last node in the list.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_element(self, value, index):
        """
        Insert a new element at the specified index in the list.

        Args:
            value: The value to be inserted.
            index (int): The position at which to insert the new element.

        Returns:
            str: "Not possible" if the insertion is not possible at the given index.
        """
        new_node = Node(value)

        # Case 1: If the head is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        # Case 2: Replacing the head with a new element
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.head.next.prev = self.head
            return

        else:
            current_node = self.head

            for _ in range(1, index):
                if not current_node:
                    return "Not possible"

                current_node = current_node.next

        # Case 3: We are adding the node at the end
            if not current_node.next:
                current_node.next = new_node
                new_node.prev = current_node
                self.tail = new_node
                return

        # Case 4: We are adding the node in the middle
        next_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        new_node.next = next_node
        next_node.prev = new_node
        return

    def remove_element(self, index):
        """
        Remove an element at the specified index from the list.

        Args:
            index (int): The position of the element to be removed.

        Returns:
            str: "No elements remaining" if the list is empty.
                 "Not possible" if the removal is not possible at the given index.
        """
        # Case 1: There are no elements present
        if not self.head:
            return "No elements remaining"

        # Case 2: We are removing the head
        if index == 0:
            temp = self.head
            next_node = temp.next
            self.head = next_node

            del temp
            self.head.prev = None
            return

        current_node = self.head

        # Since we need to remove the nth index, we use `index+1`
        for _ in range(1, index + 1):
            if not current_node.next:
                return "Not possible"
            current_node = current_node.next

        # Case 3: Removing the tail element
        if not current_node.next:
            prev_node = current_node.prev
            self.tail = prev_node
            self.tail.next = None
            del current_node
            return

        prev_node = current_node.prev
        next_node = current_node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        del current_node
        return

    def traverse_forward(self):
        """
        Traverse the list from head to tail and return a string representation.

        Returns:
            str: A string representation of the list elements connected by " <-> ".
        """
        result = ""

        current_node = self.head

        while current_node:
            result += f"{current_node.value} <-> " if current_node.next is not None else f"{current_node.value}"
            current_node = current_node.next

        return result

    def traverse_backward(self):
        """
        Traverse the list from tail to head and return a string representation.

        Returns:
            str: A string representation of the list elements connected by " <-> ".
        """
        result = ""
        current_node = self.tail

        while current_node:
            result += f"{current_node.value} <-> " if current_node.prev is not None else f"{current_node.value}"
            current_node = current_node.prev

        return result


if __name__ == "__main__":
    double_ll = DoubleLinkedList()
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