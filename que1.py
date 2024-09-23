class MinHeap:
    def __init__(self, key=lambda x: x):
        self.heap = []
        self.key = key

    def parent(self, i):
        return (i - 1) >> 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i):
        smallest = i
        left, right = self.left_child(i), self.right_child(i)
        
        if left < len(self.heap) and self.key(self.heap[left]) < self.key(self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.key(self.heap[right]) < self.key(self.heap[smallest]):
            smallest = right
        
        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heap = arr[:]
        for i in range(len(arr) // 2, -1, -1):
            self.heapify(i)

    def pop_root(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def insert(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.key(self.heap[i]) < self.key(self.heap[parent]):
            self.swap(i, parent)
            self._sift_up(parent)

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def __str__(self):
        return str(self.heap)

# Examples demonstrating ALL functionality
if __name__ == "__main__":
    print("Integer MinHeap:")
    int_heap = MinHeap()
    
    # build_min_heap
    int_heap.build_min_heap([4, 1, 7, 3, 8, 5])
    print(f"After build_min_heap: {int_heap}")
    
    # insert
    int_heap.insert(2)
    print(f"After insert 2: {int_heap}")
    
    # pop_root
    print(f"pop_root: {int_heap.pop_root()}")
    print(f"After pop_root: {int_heap}")
    
    # is_empty
    print(f"Is heap empty? {int_heap.is_empty()}")
    
    # size
    print(f"Heap size: {int_heap.size()}")
    
    # peek
    print(f"peek: {int_heap.peek()}")

    print("\nFloat MinHeap:")
    float_heap = MinHeap()
    float_heap.build_min_heap([4.5, 1.2, 7.8, 3.1, 8.9, 5.4])
    print(f"Initial heap: {float_heap}")
    float_heap.insert(2.7)
    print(f"After insert 2.7: {float_heap}")
    print(f"pop_root: {float_heap.pop_root()}")
    print(f"Heap after pop_root: {float_heap}")

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person({self.name}, {self.age})"

    print("\nCustom Object MinHeap (by age):")
    person_heap = MinHeap(key=lambda x: x.age)
    person_heap.build_min_heap([
        Person("Sreya", 30),
        Person("Nandu", 25),
        Person("Bhavya", 35),
        Person("Sravya", 20)
    ])
    print(f"Initial heap: {person_heap}")
    
    person_heap.insert(Person("Ravi", 28))
    print(f"After insert Ravi: {person_heap}")
    
    print(f"pop_root: {person_heap.pop_root()}")
    print(f"Heap after pop_root: {person_heap}")
    
    print(f"Is heap empty? {person_heap.is_empty()}")
    print(f"Heap size: {person_heap.size()}")
    print(f"peek: {person_heap.peek()}")

    # Demonstrate emptying the heap
    print("\nEmptying the heap:")
    while not person_heap.is_empty():
        print(f"pop_root: {person_heap.pop_root()}")
    print(f"Is heap now empty? {person_heap.is_empty()}")