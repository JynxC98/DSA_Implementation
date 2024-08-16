"""
Python implementation of a double linked list
"""


# Defining the node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def insert_element(self, value, index):
        new_node = Node(value)
        
        # case 1: When the list is empty
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
            
        # Case 2: We are replacing the head value
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.head.prev = None
            return
        
        else:
            current_node = self.head
            
            # Since the indexation starts from 0
            for _ in range(index - 1):
                if not current_node.next:
                    return "Not enough elements"
                    
                current_node = current_node.next
            
        # Case 3: We are adding it to the end
            if current_node.next is None:
                current_node.next = new_node
                new_node.prev = current_node
                self.tail = new_node
                
                return
            
        # Case 4: We are adding it in the middle
        
            next_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = next_node
            next_node.prev = new_node
            
            return
        
    def remove_element(self, index):
        
        current_node = self.head
        # Case 1: We are removing the head
        if index == 0:
            next_node = current_node.next
            self.head = next_node
            del current_node
            return
        
        for _ in range(index - 1):
            if not current_node:
                return "Not possible"
            current_node = current_node.next
            
        
        # Case 2: We are removing the tail
        if current_node.next is None:
            prev_node = current_node.prev
            self.tail = prev_node
            del current_node
            return
        
        # Case 3: We are removing an element from the middle
        next_node = current_node.next
        prev_node = current_node.prev
        
        prev_node.next = next_node
        next_node.prev = prev_node
        del current_node
        return
    
    def traverse_forward(self):
        result = ""
        
        current_node = self.head
        
        while current_node:
            result += f"{current_node.value} <-> " if current_node.next is not None else f"{current_node.value}"
            current_node = current_node.next
            
        return result
        
    def traverse_backward(self):
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
    double_ll.remove_element(4)
    print(double_ll.traverse_backward())
            
            
        
            
            
                
                
                
                
                
                
                
                
                
                
                
                
                