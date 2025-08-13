# Two Pointers / Sliding Window Cheatsheet

Patterns
- Strict two pointers: one leftward, one rightward
- Flexible window: both move; maintain validity by shrinking from left

Template (variable window)
- Initialize l=0, r=-1; expand r while valid; update result; if l>r then reset (l++, r=l-1); else shrink by l++ and maintain counts

Counting variants
- Count of subarrays with property <=k; derive >=, >, == via complements
- Sum of lengths: for each window length L add L*(L+1)//2 when counting all subarrays within

Tips
- For distinct elements constraints, maintain freq map and distinct count
- For sums, consider prefix-sum + hashmap alternative

Refs
- Repo Two_Pointers_Sliding_Window README

# Two Pointers / Sliding Window Cheatsheet (verbatim)

Largest subarray of 1s with at most k flips (from Two_Pointers_Sliding_Window/AZ_Method/1_Largest_Subarray_1_with_k_flips.py)
```python
def largest_subarray_1_with_k_flips(arr, k):
    n = len(arr)

    res = 0
    l,r = 0, -1  # WINDOW LENGTH = 0
    zero_count = 0

    while r < n:
        # increase right as far as possible
        while r+1<n and (arr[r+1]==1 or zero_count<k):
            r += 1
            if arr[r] == 0: zero_count += 1
        
        res = max(res, r-l+1)

        if l>r: # WINDOW LENGTH = 0 -> RESET WINDOW
            l += 1
            r = l-1
        else:
            # increment left now
            if arr[l] == 0: zero_count -= 1
            l += 1

    return res
```

Count subarrays with distinct elements <= k (from Two_Pointers_Sliding_Window/AZ_Method/2_Num_subarrays_with_distinct_elements_less_k.py)
```python
def distinct_eles_less_than_k(arr: list[int], k: int) -> int:
    n = len(arr)
    res = 0
    l,r = 0, -1

    hmap = {}

    while r<n:
        print("=>", l, r, hmap)
        # move right as far as possible
        while r+1<n and (arr[r+1] in hmap or len(hmap)<k):
            r += 1
            hmap[arr[r]] = hmap.get(arr[r],0)+1

        res += (r-l+1) # num of subarrays starting at l and ending at r

        if l>r: # 0 items in subarray
            l += 1
            r = l-1
        else:
            hmap[arr[l]] -= 1
            if hmap[arr[l]] == 0:
                hmap.pop(arr[l])
            l += 1
            
        print("<=", l, r, hmap)
    
    return res
```

Longest distinct subarray (from Two_Pointers_Sliding_Window/AZ_Method/Longest_distinct_subarray.py)
```python
def solve(arr,n):
    res = 0
    l,r = 0, -1
    hset = set()

    while r<n:
        while r+1<n and arr[r+1] not in hset:
            r += 1
            hset.add(arr[r])
        
        res = max(res, len(hset))

        if l>r:
            l += 1
            r = l-1
        else:
            hset.remove(arr[l])
            l += 1
    return res
```

3-sum nearest (two pointers after sorting) (from Two_Pointers_Sliding_Window/AZ_Method/Nearest_3_sum.py)
```python
def get_nearest_3sum(arr, target):
    n = len(arr)
    min_abs_diff = float("inf")

    arr.sort()
    for i in range(n-2):
        lo, hi = i+1, n-1
        while lo<hi:
            csum = arr[i] + arr[lo] + arr[hi]
            diff = abs(target - csum)
            if diff < min_abs_diff:
                min_abs_diff = diff

            if diff == 0:
                return 0
            if csum > target:
                hi -= 1
            else:
                lo += 1
    
    return min_abs_diff
```

Count subarrays with sum at most K (from Two_Pointers_Sliding_Window/AZ_Method/Num_Subarray_with_sum_atmost_K.py)
```python
def solve(arr, k):
  n = len(arr)
  l,r = 0, -1
  csum = 0
  res = 0

  while r<n:
    # move right as far as possible
    while r+1<n and (csum+arr[r+1] <= k):
      r += 1
      csum += arr[r]

    res += (r-l+1)
    
    if l>r:
      l += 1
      r = l-1
    else:
      csum -= arr[l]
      l += 1

  return res
```

Shortest subarray containing all distinct elements (from Two_Pointers_Sliding_Window/AZ_Method/Shortest_Distinct_subarray.py)
```python
ndistinct = len(set(arr))
res = n
l,r = 0, -1
hmap = {}

while r<n:
  while r+1<n and len(hmap)<ndistinct:
    r += 1
    hmap[arr[r]] = hmap.get(arr[r],0)+1
  
 
  if len(hmap) == ndistinct:
    res = min(res, r-l+1)

  if l>r:
    l += 1
    r = l-1
  else:
    hmap[arr[l]] -= 1
    if hmap[arr[l]] == 0:
      hmap.pop(arr[l])
    l += 1
```

Continuous subarrays with any pair diff <= 2 (heap-based window) (from Two_Pointers_Sliding_Window/AZ_Method/Subarrays_with_any_pair_sum_less_than_k.py)
```python
from queue import PriorityQueue
from typing import List

class Solution:
    def continuousSubarrays(self, arr: List[int]) -> int:
        k = 2  # Maximum allowed difference between min and max
        minh = PriorityQueue()  # Min heap
        maxh = PriorityQueue()  # Max heap
        n = len(arr)
        l, r = 0, -1  # Sliding window boundaries
        result = 0  # To count the number of valid subarrays

        while r < n - 1:
            # Expand the window
            r += 1
            minh.put((arr[r], r))
            maxh.put((-arr[r], r))

            # INCREMENT LEFT ONLY IF IT VOILATES
            while abs(minh.queue[0][0] - (-maxh.queue[0][0])) > k:
                # Contract the window from the left
                l += 1

                # Remove elements outside the window from heaps
                while not minh.empty() and minh.queue[0][1] < l:
                    minh.get()
                while not maxh.empty() and maxh.queue[0][1] < l:
                    maxh.get()

            # Count all valid subarrays ending at index `r`
            print(f"{l} -> {r}")
            result += (r - l + 1)

        return result
```

Minimum size subarray sum (from Two_Pointers_Sliding_Window/Old_Solved/Minimum_Size_Subarray_Sum.py)
```python
class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 1 if arr[0] >= target else 0

        left,right = 0,0
        res = float("inf")
        csum = arr[0]

        while left<=right and right < n:
            if arr[left] >= target or arr[right] >= target:
                return 1
            
            if csum >= target:
                res = min(res, right-left+1)
                csum -= arr[left] # first decreement and then decrease right
                left += 1
            
            else: # csum < target
                right += 1
                if right >= n:
                    break
                csum += arr[right]
        
        return res if res!=float("inf") else 0
```

---

## 🗺️ Quick map
- 🧭 Fixed vs variable windows
- ➗ Distinct counts, sums, and min/max constraints
- 🔁 Sorted two-pointers patterns (2/3-sum, nearest)

## ✅ Study checklist
- [ ] Update structures before moving l?
- [ ] atMost/exactly trick used when needed?
- [ ] Sorted precondition satisfied for two-pointer sums?
