# Stacks and Queues Cheatsheet

Stacks
- Monotonic stack for next/prev greater/less problems
- Evaluate RPN; parentheses validation; histogram max rectangle

Queues
- BFS; sliding window with deque (monotonic queue)
- Circular queue patterns

Deques
- O(1) push/pop both ends; use collections.deque

Pitfalls
- Off-by-one when using indices for next/prev boundaries

---

## At a glance
- Monotonic stacks: Next/prev greater/smaller, histogram-area, subarray min/max contributions.
- Monotonic queues (deque): Sliding window min/max in O(n).
- Parsing: Use stacks for parentheses/brackets, RPN, expression evaluation.

## Pitfalls
- For contribution problems, strictly vs non-strictly monotonic changes inclusion/exclusion of equal elements.
- For sliding windows, evict indices that fall out of range, not values.
- Be careful with duplicates in NGE/NSE—define tie-breaking consistently.

# Stacks and Queues Cheatsheet (verbatim)

Sliding Window Maximums (Monotonic Deque) (from Stacks_Queues/Monotonic_Incr_Decr_Queue/Sliding_Window_Maximums.py)
```python
from collections import deque

class Ele:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = deque()
        res = []
        
        l,r = 0,0

        while r<n:
            # before inserting make sure all element in Q <= curr
            while len(q) != 0 and q[-1].val <= arr[r]:
                q.pop() # pop right
            q.append(Ele(r, arr[r]))

            # check if left needs to be popped (You have moved to next window)
            if l > q[0].idx:
                q.popleft()

            if r-l+1 >= k: # whenever your window size == k
                res.append(q[0].val)
                l += 1 # move to next window
            
            r += 1 # move to next element

        return res
```

Next Greater Element I and II (from Stacks_Queues/NGE_NLE/Next_Greater_Element_I_II.py)
```python
from typing import List

def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    n = len(arr)
    res = [-1 for _ in range(n)]
    st = []

    for i in reversed(range(n)):
        x = arr[i]
        # remove all elements > cur
        while len(st) != 0 and st[-1] <= x:
            st.pop()

        if len(st) == 0: # no NGE
            res[i] = -1
        else: # NGE = stack.top()
            res[i] = st[-1]
        st.append(x) # add cur element

    return res

def nextGreaterElementCircular(arr: List[int], n: int) -> List[int]:
    n = len(arr)
    res = [-1 for _ in range(n)]
    st = []

    for i in reversed(range(2*n)):
        x = arr[i%n]

        while len(st) != 0 and st[-1] <= x:
            st.pop()

        if i<n:
            if len(st) == 0:
                res[i] = -1
            else:
                res[i] = st[-1]

        # keep on adding curr
        st.append(x)

    return res
```

Largest Rectangle in Histogram (from Stacks_Queues/NGE_NLE/Area_of_largest_rectangle.py)
```python
class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)

        # first smaller element in left side, save index -> MODIFIED NGE/NSE
        lsmall = [-1 for _ in range(n)]
        st = []
        for i in range(n):
            while len(st) != 0 and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st)!=0:
                lsmall[i] = st[-1]
            st.append(i)

        # first smaller element in right side, save index -> MODIFIED NGE/NSE
        rsmall = [-1 for _ in range(n)] 
        st = []
        for i in reversed(range(n)):
            while len(st) != 0 and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st)!=0:
                rsmall[i] = st[-1]
            st.append(i)

        res = 0
        for i in range(n):
            lbh = lsmall[i]+1 if lsmall[i]!=-1 else 0
            rbh = rsmall[i]-1 if rsmall[i]!=-1 else n-1
            res = max(res, (rbh-lbh+1)*arr[i])
        
        return res
```

---

## 🗺️ Quick map
- 🧱 Monotonic stack/queue use-cases
- 🪟 Sliding window with deque
- ✍️ Expression/parentheses parsing

## ✅ Study checklist
- [ ] Strict vs non-strict monotonic chosen for duplicates?
- [ ] Evict by index, not value, in windows?
- [ ] Edge cases covered (empty stack, boundaries)?
