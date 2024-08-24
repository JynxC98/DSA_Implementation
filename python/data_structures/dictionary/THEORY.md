# HashMap: Concise Guide

## Definition

A HashMap is a data structure that implements an associative array abstract data type, allowing for efficient mapping of keys to values. It uses a hash function to compute an index into an array of buckets, from which the desired value can be found.

## Collisions in HashMaps

A collision occurs when two different keys hash to the same index in the HashMap's underlying array.

### What Causes Collisions?

1. Limited array size: The number of possible keys often exceeds the array size.
2. Imperfect hash functions: Even good hash functions can sometimes produce the same output for different inputs.


## Basic Operations and Time Complexities

### 1. put(key, value)

Adds a key-value pair to the HashMap or updates the value if the key already exists.

- **Average Time Complexity**: O(1)
- **Worst Time Complexity**: O(n) (when many collisions occur)

### 2. get(key)

Retrieves the value associated with the given key.

- **Average Time Complexity**: O(1)
- **Worst Time Complexity**: O(n) (when many collisions occur)

### 3. remove(key)

Removes the key-value pair associated with the given key.

- **Average Time Complexity**: O(1)
- **Worst Time Complexity**: O(n) (when many collisions occur)

### 4. containsKey(key)

Checks if the HashMap contains the given key.

- **Average Time Complexity**: O(1)
- **Worst Time Complexity**: O(n) (when many collisions occur)

### 5. size()

Returns the number of key-value pairs in the HashMap.

- **Time Complexity**: O(1)

### 6. isEmpty()

Checks if the HashMap is empty.

- **Time Complexity**: O(1)

### 7. clear()

Removes all key-value pairs from the HashMap.

- **Time Complexity**: O(n), where n is the capacity of the HashMap

## Load Factor and Resizing

The load factor is the ratio of the number of stored key-value pairs to the number of buckets. When it exceeds a threshold (typically 0.75), the HashMap is resized to maintain efficiency.

- **Time Complexity of Resizing**: O(n), where n is the number of key-value pairs

## Space Complexity

The space complexity of a HashMap is O(n), where n is the number of key-value pairs stored.

## Collision Resolution Strategies

1. **Chaining**: Each bucket contains a list of entries. 
   - Worst-case time complexity for operations becomes O(n) if all keys collide.

2. **Open Addressing**: Probes for next open slot in the bucket array.
   - Maintains O(1) average time complexity but may degrade with increased load factor.

## Factors Affecting Performance

1. **Hash Function Quality**: A good hash function distributes keys uniformly.
2. **Initial Capacity**: Appropriate initial size can reduce the need for early resizing.
3. **Load Factor**: Lower load factor generally means fewer collisions but more space overhead.

## Use Cases

1. Caching
2. Database indexing
3. Counting frequency of items
4. Implementing associative arrays
5. Solving substring problems in string algorithms

## Advantages

1. Fast average-case lookups: O(1) for basic operations
2. Flexible keys: Can use various data types as keys
3. Unordered: No need to maintain any order, improving performance

## Disadvantages

1. Collisions can lead to worst-case O(n) time complexity
2. Space overhead for storing buckets
3. No inherent ordering of elements