# Data-Structures-Basics

This repository contains implementations of fundamental data structures to demonstrate core programming skills, focusing on understanding how data is organized and manipulated dynamically in memory.

## Singly Linked List

A **Singly Linked List** is a linear data structure where each element (called a node) contains data and a reference (pointer) to the next node in the sequence. This allows efficient insertion and deletion of elements without shifting other elements, unlike arrays.

### What This Implementation Does:

- Defines a `Node` class representing an individual element with:
  - `data`: the value stored
  - `next`: a reference to the next node (or `None` if it’s the last node)
  
- Defines a `SinglyLinkedList` class that manages the list with the following methods:
  - `append(data)`: Adds a new node containing `data` to the end of the list.
  - `delete(key)`: Removes the first node found with the value `key`.
  - `display()`: Prints the entire list in order from head to tail.
  
- Demonstrates:
  - Creating a linked list and appending multiple values
  - Deleting an existing value
  - Attempting to delete a value not present in the list
  - Traversing and printing the list contents

### Why Use a Linked List?

- Efficient insertion and deletion at any position without reallocating or shifting other elements.
- Useful for implementing other data structures like stacks, queues, and graphs.
- Helps understand pointers/references and dynamic memory usage.

### How to Run

1. Make sure you have Python 3 installed on your machine.
2. Clone or download this repository.
3. Run the script from the command line:

```bash
python linked_list.py
