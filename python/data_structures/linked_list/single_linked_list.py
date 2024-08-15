"""
Implementation of a single linked list
"""

class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node in the linked list.
    """

    def __init__(self, value):
        """
        Initialize a new node.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: The first node in the linked list.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_element(self, value, index):
        """
        Insert a new element at the specified index in the linked list.

        Args:
            value: The value to be inserted.
            index (int): The position at which to insert the new element.

        Returns:
            str: "Invalid position" if the index is out of bounds.

        Time complexity: O(n), where n is the number of nodes in the list.
        Space complexity: O(1)
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                return

            current_node = self.head
            for _ in range(index - 1):
                if not current_node.next:  # Handle out of bounds
                    return "Invalid position"
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

    def delete_element(self, index):
        """
        Delete the element at the specified index in the linked list.

        Args:
            index (int): The position of the element to be deleted.

        Returns:
            str: "Not possible" if the list is empty or the index is out of bounds.

        Time complexity: O(n), where n is the number of nodes in the list.
        Space complexity: O(1)
        """
        if not self.head:
            return "Not possible"

        if index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            current_node = self.head
            for _ in range(index - 1):
                if not current_node.next:  # Handle out of bounds
                    return "Not possible"
                current_node = current_node.next

            temp = current_node.next
            if temp:
                current_node.next = temp.next
                del temp
            else:
                return "Not possible"  # If trying to delete a non-existent element

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.

        Time complexity: O(n), where n is the number of nodes in the list.
        Space complexity: O(n)
        """
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)

if __name__ == "__main__":
    # Example usage
    linked_list = LinkedList()
    linked_list.insert_element(20, 0)
    linked_list.insert_element(30, 1)
    linked_list.insert_element(40, 2)
    linked_list.insert_element(1000, 3)
    linked_list.insert_element(54, 2)
    print(linked_list)  # [20, 30, 54, 40, 1000]

    linked_list.delete_element(3)
    print(linked_list)  # [20, 30, 54, 1000]

    linked_list.delete_element(4)
    print(linked_list)  # "Not possible" since index 4 is out of bounds