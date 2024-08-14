# Array Data Structure

## Definition

An **array** is a linear data structure that stores a collection of elements, typically of the same data type, in a contiguous block of memory. Each element in the array can be accessed by its index, which is an integer value representing its position within the array. Arrays are one of the most fundamental and widely used data structures in computer science due to their efficiency in accessing and manipulating data.

## Memory Allocation

In memory, an array is allocated as a continuous block where each element is stored next to the others. The size of the array is determined at the time of its creation and cannot be changed during runtime (in static arrays). The amount of memory allocated for an array depends on the data type of the elements and the number of elements the array will hold.

### Example:

For an array of integers with 4 elements:
- If each integer takes up 4 bytes of memory, the total memory required is `4 elements * 4 bytes = 16 bytes`.



## Methods

Common operations on arrays include:

1. **Accessing elements**: O(1) time complexity
2. **Insertion**: 
   - At the end (if space available): O(1)
   - At a specific index: O(n)
3. **Deletion**: 
   - From the end: O(1)
   - From a specific index: O(n)
4. **Searching**: 
   - Unsorted array: O(n)
   - Sorted array (binary search): O(log n)
5. **Traversal**: O(n)

