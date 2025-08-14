"""
GREAT DOC: https://bradfieldcs.com/algos/trees/priority-queues-with-binary-heaps/

====== MIN HEAP ======
INTUITION:
=> Complete Binary Tree
- Represent the heap as a Complete Binary Tree using a LIST (nodes filled level by level).
- In CBT, node at index i has:
    left child  = 2*i
    right child = 2*i + 1
    parent      = i // 2
- We use items = [0] as a dummy index so the math is cleaner (1-based indexing).

=> MIN HEAP PROPERTY
- Parent(items[i]) must be smaller than both children.

=> INSERT(val)
- Insert at the end.
- Propagate UP: swap with parent while property is violated.

=> PEEK
- Return items[1] (min element).

=> POP
- Remove root (items[1]).
- Replace it with last element.
- Propagate DOWN: swap with smaller child while property is violated.

==> TIME COMPLEXITIES
- peek   -> O(1)
- insert -> O(log n)
- pop    -> O(log n)
- build  -> O(n) if heapify, O(n log n) if inserting each.
"""


class MinHeap:
    def __init__(self):
        self.items = [0]  # dummy index for easy math
        self.size = 0

    def _propagate_up(self):
        i = self.size
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i], self.items[i // 2] = self.items[i // 2], self.items[i]
            i //= 2

    def _propagate_down(self):
        i = 1
        while i * 2 <= self.size:  # while left child exists
            min_child = self._get_min_child(i)
            if self.items[i] > self.items[min_child]:
                self.items[i], self.items[min_child] = self.items[min_child], self.items[i]
            i = min_child

    def _get_min_child(self, i):
        if i * 2 + 1 > self.size:  # no right child
            return i * 2
        else:  # both children exist
            if self.items[i * 2] < self.items[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, val):
        self.items.append(val)
        self.size += 1
        self._propagate_up()

    def peek(self):
        return self.items[1] if self.size > 0 else None

    def pop(self):
        if self.size == 0:
            return None
        root_val = self.items[1]
        self.items[1] = self.items[self.size]
        self.items.pop()
        self.size -= 1
        if self.size > 0:
            self._propagate_down()
        return root_val


class MaxHeap:
    def __init__(self):
        self.items = [0]
        self.size = 0

    def _propagate_up(self):
        i = self.size
        while i // 2 > 0:
            if self.items[i] > self.items[i // 2]:
                self.items[i], self.items[i // 2] = self.items[i // 2], self.items[i]
            i //= 2

    def _propagate_down(self):
        i = 1
        while i * 2 <= self.size:
            max_child = self._get_max_child(i)
            if self.items[i] < self.items[max_child]:
                self.items[i], self.items[max_child] = self.items[max_child], self.items[i]
            i = max_child

    def _get_max_child(self, i):
        if i * 2 + 1 > self.size:  # no right child
            return i * 2
        else:
            if self.items[i * 2] > self.items[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, val):
        self.items.append(val)
        self.size += 1
        self._propagate_up()

    def peek(self):
        return self.items[1] if self.size > 0 else None

    def pop(self):
        if self.size == 0:
            return None
        root_val = self.items[1]
        self.items[1] = self.items[self.size]
        self.items.pop()
        self.size -= 1
        if self.size > 0:
            self._propagate_down()
        return root_val


# Example usage:
if __name__ == "__main__":
    print("=== MinHeap ===")
    minh = MinHeap()
    for x in [10, 20, 15, 5, 8, 1]:
        minh.insert(x)
        print(minh.items)
    while minh.size:
        print("Pop:", minh.pop(), "| Heap:", minh.items)

    print("\n=== MaxHeap ===")
    maxh = MaxHeap()
    for x in [10, 20, 15, 5, 8, 1]:
        maxh.insert(x)
        print(maxh.items)
    while maxh.size:
        print("Pop:", maxh.pop(), "| Heap:", maxh.items)
