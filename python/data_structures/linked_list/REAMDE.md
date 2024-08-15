# Linked List Documentation

## Definition
A **linked list** is a linear data structure that consists of a sequence of elements, known as nodes. Each node contains two main components:
1. **Data**: The value or information the node holds.
2. **Pointer/Reference**: A link to the next node in the sequence.

Unlike arrays, linked lists do not require contiguous memory allocation, allowing for dynamic memory usage and efficient insertions and deletions.

## Types of Linked Lists
1. **Singly Linked List**: Each node points to the next node and the last node points to `null`.
2. **Doubly Linked List**: Each node contains a pointer to both the next and previous nodes, allowing traversal in both directions.
3. **Circular Linked List**: The last node points back to the first node, forming a circle. This can be implemented in both singly and doubly linked lists.

## Data Storage
In a linked list, data is stored in nodes. Each node is typically structured as follows:

```plaintext
+-------+-------+
| Data  | Next  |
+-------+-------+
```
Example of a single linked list
```plaintext
Head -> [Data|Next] -> [Data|Next] -> [Data|Next] -> null
```
Example of a double linked list
```plaintext
null <- [Prev|Data|Next] <-> [Prev|Data|Next] <-> [Prev|Data|Next] -> null
```
#### Common methods and the time complexities
1. **Insertion**
    - At the Beginning: $O(1)$
    - At the End: $O(n)$ for singly linked lists ($O(1)$ for doubly linked lists if we maintain a tail pointer)
    - At a Given Position: $O(n)$
1. **Deletion**
    - From the Beginning: $O(1)$
    - From the End: $O(n)$ for singly linked lists ($O(1)$ for doubly linked lists if we maintain a tail pointer)
    - From a Given Position: $O(n)$
1. **Searching**
    - Search for a value: $O(n)$
1. **Traversal**
    - Traverse the list: $O(n)$

#### Advantages of a linked list:
1. Dynamic Size: They can grow and shrink in size as needed.
1. Efficient Insertions/Deletions: Particularly at the beginning or end of the list.