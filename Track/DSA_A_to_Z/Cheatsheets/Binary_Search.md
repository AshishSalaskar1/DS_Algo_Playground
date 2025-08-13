# Binary Search Cheatsheet

Patterns (from repo)
- Binary search on answers (e.g., Koko Eating Bananas)
- Lower/upper bound and boundary-finding (see folder for problems like First/Last Occurrence)

Koko Eating Bananas (from Binary Search/Koko_Eating_Bananas.py)
```python
import math
class Solution:
    def is_possible(self, arr, hrs, speed):
        hrs_taken = sum([math.ceil(x/speed) for x in arr])
        print(speed, hrs_taken, hrs)
        return hrs_taken <= hrs

    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        lo, hi = 1, max(arr)
        res = float("inf")
        

        while lo<=hi:
            mid = lo + (hi-lo)//2
            # print("=>", lo, mid, hi)
            if self.is_possible(arr, h, mid):
                # print(mid)
                res = min(res, mid)
                hi = mid-1
            else:      
                lo = mid+1
        
        return res if res != float("inf") else -1
```

Refer to repo files for more patterns:
- Book_Allocation_Problem.py, Painters_Partition.py (BS on answers)
- First_and_last_occurence_of_number.py, Floor_and_Ceil.py (bounds)
- Minimum_in_Sorted_Rotated_Array.py, Bin_Search_Sorted_Rotated_Array.py (rotated arrays)
- Smallest_Divisor_given_threshold.py, Capacity_to_ship_packages.py (feasibility)

---

## At a glance
- Patterns: on-index (find first/last), on-answer (min feasible / max feasible) using monotonic predicate.
- Mid: mid = l + (r-l)//2 avoids overflow (conceptually relevant across languages).
- Update rules: Decide inclusive/exclusive carefully. Common: if feasible -> r = mid; else -> l = mid+1 for lower_bound.
- Termination: Prefer while l < r for lower_bound/upper_bound flavors; while l <= r when returning mid during loop.

## Pitfalls
- Infinite loops from wrong mid/update combo (e.g., using mid when l+1==r and not moving).
- Duplicates: lower_bound vs upper_bound semantics.
- On-answer: ensure predicate is monotonic and boundaries cover impossible/guaranteed zones.

---

## 🗺️ Quick map
- 🎯 On-index: lower/upper bound, first/last true
- 📏 On-answer: monotonic predicate + bounds
- 🧭 Termination patterns and off-by-one guards

## ✅ Study checklist
- [ ] Is predicate truly monotonic?
- [ ] Are bounds inclusive/exclusive decided upfront?
- [ ] While condition and mid update avoid infinite loop?
- [ ] Duplicates handled with lower/upper correctly?
