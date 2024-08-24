# Theory of Trees

## Table of Contents

1. **Introduction**
2. **Basic Terminology**
3. **Tree Properties**
4. **Types of Trees**
   - 4.1 Binary Trees
   - 4.2 Binary Search Trees (BST)
   - 4.3 Balanced Trees
   - 4.4 AVL Trees
   - 4.5 Red-Black Trees
   - 4.6 B-Trees
   - 4.7 Tries (Prefix Trees)
5. **Tree Traversal Techniques**
6. **Applications of Trees**
---

## 1. Introduction

A **tree** is an abstract model of a hierarchical structure, a set of nodes connected by edges. Unlike linear data structures such as arrays, linked lists, stacks, and queues, which organize data in a sequential manner, trees store data in a non-linear fashion. This characteristic makes them ideal for representing hierarchies and relationships in a multitude of domains, including computer science, mathematics, and biology.

Trees are fundamental to various algorithms and systems, including file systems, databases, and parsing algorithms. Their hierarchical nature allows for efficient searching, insertion, and deletion operations, which is why they are a cornerstone in algorithm design and implementation.

---

## 2. Basic Terminology

Understanding the terminology associated with trees is crucial for grasping more advanced concepts. Below are the fundamental terms:

- **Node**: A basic unit of a tree, containing data and references (links) to its children.
- **Edge**: A connection between two nodes. If node A is connected to node B, there is an edge between A and B.
- **Root**: The top node in a tree. It is the only node with no parent, serving as the origin of traversal.
- **Leaf**: A node with no children, also known as a terminal node.
- **Parent**: A node that has one or more children. 
- **Child**: A node that descends from another node. If B is a child of A, then A is the parent of B.
- **Subtree**: A tree formed by a node and its descendants.
- **Ancestor and Descendant**: If there is a path from node A to node B, then A is an ancestor of B, and B is a descendant of A.
- **Siblings**: Nodes that share the same parent.
- **Forest**: A collection of disjoint trees.

---

## 3. Tree Properties

- **Height of a Tree**: The length of the longest path from the root to a leaf. It is a key measure, influencing the efficiency of various tree operations.
- **Depth of a Node**: The length of the path from the root to that node. The root node has a depth of 0.
- **Level of a Node**: The depth of a node plus one. Nodes at the same depth are said to be on the same level.
- **Degree of a Node**: The number of children a node has.
- **Balanced Tree**: A tree where the heights of the two subtrees of any node differ by at most one.
- **Full Tree**: A tree in which every node other than the leaves has two children.
- **Complete Tree**: A binary tree in which all levels, except possibly the last, are fully filled, and all nodes are as far left as possible.

---

## 4. Types of Trees

### 4.1 Binary Trees

A **Binary Tree** is a tree where each node has at most two children, often referred to as the left child and the right child. Binary trees are foundational in understanding more complex tree structures.

### 4.2 Binary Search Trees (BST)

A **Binary Search Tree (BST)** is a binary tree where each node's left subtree contains only nodes with values less than the node's value, and the right subtree contains only nodes with values greater than the node's value. This property makes BSTs efficient for search operations.

### 4.3 Balanced Trees

A **Balanced Tree** is a tree where the height of the two subtrees of every node never differs by more than one. Balanced trees ensure that operations such as insertion, deletion, and search are performed in optimal time.

### 4.4 AVL Trees

An **AVL Tree** is a self-balancing binary search tree where the difference in heights of left and right subtrees for every node is at most one. Named after its inventors, Adelson-Velsky and Landis, AVL trees are one of the first dynamically balanced trees.

### 4.5 Red-Black Trees

A **Red-Black Tree** is a self-balancing binary search tree where nodes have an extra bit for denoting the color of the node, either red or black. The colors ensure that the tree remains balanced during insertions and deletions.

### 4.6 B-Trees

A **B-Tree** is a self-balancing search tree in which nodes can have multiple children. B-Trees are widely used in databases and file systems, where data is stored in blocks or pages.

### 4.7 Tries (Prefix Trees)

A **Trie** (pronounced "try"), also known as a **Prefix Tree**, is a tree used to store a dynamic set or associative array where the keys are usually strings. Tries are highly efficient for tasks like autocomplete and spell-checking.

---

## 5. Tree Traversal Techniques

Tree traversal refers to the process of visiting each node in a tree in a specific order. The most common traversal methods are:

- **Pre-order Traversal**: Visit the root node, traverse the left subtree, then traverse the right subtree.
- **In-order Traversal**: Traverse the left subtree, visit the root node, then traverse the right subtree.
- **Post-order Traversal**: Traverse the left subtree, traverse the right subtree, then visit the root node.
- **Level-order Traversal**: Visit nodes level by level, starting from the root, and moving from left to right.

---

## 6. Applications of Trees

Trees have a wide range of applications, including but not limited to:

- **Hierarchical Data Representation**: Used in representing organizational structures, file systems, and taxonomies.
- **Database Indexing**: B-Trees and their variants are used to maintain balanced and efficient access to databases.
- **Routing Algorithms**: Trees, particularly spanning trees, are essential in network routing algorithms.
- **Parsing Expressions**: Abstract Syntax Trees (ASTs) are used in compilers and interpreters to represent the structure of program code.
- **Decision Trees**: Used in machine learning for classification and regression tasks.

---