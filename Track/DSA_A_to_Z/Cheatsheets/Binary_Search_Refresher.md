# Binary Search Refresher

Problem types
1) Base variations (left/right movement by local pattern)
2) Binary search on answers (feasible window/limit)
3) Third-array generation using two arrays (never build C)
4) BS for each start index

0/1 boundary thinking
- Convert array relation into a 0/1 monotone mask, then find leftmost/rightmost 1
- Examples
  - Rotations count: rightmost 1 where arr[i] < arr[0]
  - Bitonic peak: leftmost 1 where arr[i] >= arr[i+1]

Notes
- Apply convert(mid) directly so runtime remains O(log n)
- Focus on pattern around mid, not only equality

---

## 🗺️ Quick map
- 🎯 Templates: lower_bound, upper_bound, first/last true
- 🧭 On-answer search with monotonic predicate
- 🧪 Test harness tips and boundary stress tests

## ✅ Study checklist
- [ ] Predicate monotonic and total over [lo, hi]?
- [ ] Inclusive/exclusive bounds decided upfront?
- [ ] Termination condition prevents infinite loops?
- [ ] Duplicates handled (lower vs upper) per problem?
