# General CP/DSA Notes

Python tips
- input() is slow; prefer sys.stdin.readline
- Function scope gives small speedup vs top-level
- String concat s+=t can be faster than s=s+t

Bisect
- bisect_right ≡ upper_bound, bisect_left ≡ lower_bound; insort/insort_left insert while sorted

Modulo
- (a+b)%m, (a-b+m)%m, (a/b)%m == a% m * inv(b)%m
- Fermat inv: a^(m-2) % m (m prime)
- Python negative mod caution → use (x%m + m)%m when needed

Data structures
- PriorityQueue (min-heap); for max-heap push -x and pop then negate
- deque for O(1) push/pop ends

Magic methods
- __gt__ for custom comparisons; __repr__ for printing

Docs and lists
- Leetcode topic lists and study guides (see repo root README)

---

## 🗺️ Quick map
- 🧠 Mental models and common traps
- 🧰 Cross-topic tricks (prefix, hashing, compression)
- 🧪 Debug checklists

## ✅ Study checklist
- [ ] Define state/variables and invariants first
- [ ] Small counterexample for each assumption
- [ ] Print minimal traces; test boundaries explicitly
