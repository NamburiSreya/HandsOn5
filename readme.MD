**MinHeap Implementation in Python**

**Overview**

This project implements a Min Heap data structure in Python. A Min Heap is a binary tree where each parent node is smaller than or equal to its children, making it efficient for priority queue operations.

**Features**

- Generic implementation supporting various data types
- Build a min heap from an array
- Insert new elements
- Remove and return the smallest element (root)
- Peek at the root element
- Check if the heap is empty
- Get the size of the heap

**Usage**

The MinHeap class provides the following main methods:

-build_min_heap(arr): Constructs a min heap from a given array
- insert(item): Adds a new item to the heap
- pop_root(): Removes and returns the smallest element
- peek(): Returns the smallest element without removing it
- is_empty(): Checks if the heap is empty
- size(): Returns the number of elements in the heap

**Implementation Details**

- Uses bit manipulation for parent and child index calculations
- Implements heapify-up and heapify-down procedures
- Allows custom comparison keys for complex objects
