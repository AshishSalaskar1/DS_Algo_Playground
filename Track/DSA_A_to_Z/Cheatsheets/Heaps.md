# Heaps Cheatsheet

Basics
- Min-heap is default; for max-heap push negatives or use key wrappers
- Top-k elements; kth element; merging k sorted lists

PriorityQueue vs heapq
- queue.PriorityQueue is thread-safe; heapq is faster for CP
- Items must be comparable; use tuples (key, tie-breaker)

Operations
- push O(log n), pop O(log n), heapify O(n)

Pitfalls
- Keep memory in check for streaming problems (bounded-size heaps)

---

## At a glance
- Top-K/Kth: Maintain size-k heap; min-heap for kth largest; max-heap for kth smallest.
- Streaming medians: Two heaps (low max-heap, high min-heap), rebalance size diff ≤1.
- Dijkstra/Prim: Use heap of (key,node); skip stale entries with visited/distance checks.

## Pitfalls
- Python’s heapq is min-heap; simulate max-heap with negation.
- Lazy deletion: when removing arbitrary items from heaps, track validity (index or timestamp) and discard stale tops.

# Heaps Cheatsheet (verbatim)

Kth largest element (from Heaps/K_largest_element.py)
```python
from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        pq = PriorityQueue()
        for num in nums:
            pq.put(num)
            if pq.qsize() > k:
                pq.get()
        return pq.get()
```

---

## 🗺️ Quick map
- 🥇 K-th / Top-K patterns
- ⚖️ Streaming medians (two heaps)
- 🧭 Graph algos (Dijkstra/Prim) heap tips

## ✅ Study checklist
- [ ] Min-heap vs max-heap choice correct?
- [ ] Lazy deletion/stale entries handled?
- [ ] Rebalancing invariant in two-heaps kept?
