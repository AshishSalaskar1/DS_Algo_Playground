# Greedy Cheatsheet

When it works
- Exchange argument or matroid-like independence; local optimal choices lead to global optimum

Common patterns
- Intervals: sort by finish/start; activity selection; minimum arrows; merge intervals
- Scheduling: earliest deadline first; shortest job first (with heap)
- Huffman coding: combine two smallest repeatedly (heap)

Pitfalls
- Validate optimality; counterexamples often exist
- Sorting criterion correctness

---

## At a glance
- Greedy schema: Define a local choice that’s globally optimal (exchange argument / matroid or interval structure).
- Intervals: sort by earliest finishing time (like meetings), or appropriate key.
- Scheduling/selection: Use heaps for picking smallest/largest frontier element when order changes online.

## Pitfalls
- Prove correctness or rely on known structures (interval scheduling, Huffman coding, activity selection, Kruskal MST).
- Watch tie-breakers in sorts—they can change outcomes for equal keys.

---

## 🗺️ Quick map
- 🗂️ Interval scheduling and variants
- 🪙 Classic greedy (Huffman, Kruskal)
- 🧮 Priority-queue driven selection

## ✅ Study checklist
- [ ] Exchange argument intuition clear?
- [ ] Sort keys and tie-breakers set?
- [ ] Proof/structure (interval/matroid) recognized?

# Greedy Cheatsheet (verbatim)

N meetings in one room (from Greedy/N_meetings_in_room.py)
```python
# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

class Solution:
    def maximumMeetings(self, n : int, start : list, end : list) -> int:
        pairs = sorted([(start[i], end[i]) for i in range(n)], key=lambda x: (x[1], x[0]))

        count_meetings = 1
        prev_end = pairs[0][1]
        for i in range(1, n):
            if pairs[i][0] > prev_end:
                # select
                count_meetings += 1
                prev_end = pairs[i][1]

        return count_meetings
```
