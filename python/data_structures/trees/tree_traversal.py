"""
Implementation of different traversal methods in tree.
"""
from collections import deque

class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
        value: The value stored in the node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """
    def __init__(self, value):
        """
        Initialise a new Node.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal(root, result=None):
    """
    Perform a post-order traversal of a binary tree.

    Args:
        root (Node): The root node of the binary tree.
        result (list, optional): A list to store the traversal result. 
                                 If None, a new list is created.

    Returns:
        list: A list containing the values of the nodes in post-order.
    """
    if result is None:
        result = []
    
    if root:
        post_order_traversal(root.left, result)
        post_order_traversal(root.right, result)
        result.append(root.value)
    
    return result

def pre_order_traversal(root, result=None):
    """
    Perform a pre-order traversal of a binary tree.

    Args:
        root (Node): The root node of the binary tree.
        result (list, optional): A list to store the traversal result. 
                                 If None, a new list is created.

    Returns:
        list: A list containing the values of the nodes in pre-order.
    """
    if result is None:
        result = []
    
    if root:
        result.append(root.value)
        pre_order_traversal(root.left, result)
        pre_order_traversal(root.right, result)
    
    return result

def in_order_traversal(root, result=None):
    """
    Perform an in-order traversal of a binary tree.

    Args:
        root (Node): The root node of the binary tree.
        result (list, optional): A list to store the traversal result. 
                                 If None, a new list is created.

    Returns:
        list: A list containing the values of the nodes in in-order.
    """
    if result is None:
        result = []
        
    if root:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)
        
    return result
        
def level_order_traversal(root, result=None):
    """
    Perform a level-order traversal of a binary tree.

    Args:
        root (Node): The root node of the binary tree.
        result (list, optional): A list to store the traversal result. 
                                 If None, a new list is created.

    Returns:
        list: A list containing the values of the nodes in level-order.
    """
    if result is None:
        result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result
        

if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    # Perform and print different traversals
    print(pre_order_traversal(root))
    print(in_order_traversal(root))
    print(post_order_traversal(root))
    print(level_order_traversal(root))