"""
PROBLEM: Given two arrays A of size N and B of size M and an integer K. Create a new array C of size N*M consisting of A[i]+B[j] for 1≤i≤N, 1≤j≤M. 
Find the Kth smallest element in the array C.

Example: 
a = [1,2,3]
b = [4,5,6]
k=6
# c = [5,6,6,7,7,7,8,8,9]
RES = 7


LOGIC 1: BINARY SEARCH ON ANSWER
- check(a, b, x, k ) -> 
    1. if (num elements in `c` <=x ) >= k -> RETURN TRUE
    2. RETURN FALSE
- Why if (num elements in `c` <=x ) >= k?
    - if `x` is `k` th smallest element then for sure it will have `k-1` elements smaller than it
    - You can also have multiple elements of same val `x`, hence it can be `>=k` also

LOGIC 2: How to check (num elements in `c` <=x ) >= k
- You can manually join the arrays - SOL: UPPER_BOUND

a = [1,2,3]
b = [4,5,6]
k=6, x=7

1. From `a` you pick one element (`a[i]`) 
    - How many element from `b` can you pick such that `a[i]`+`b[j]` <= `x`
    - Ex if you pick `1` from `b` you can pick 4,5,6 (all these are <7 (7-1))
    - num picks = `upper_bound(b, x-a[i])` = num element in `b` which are `<= (x-a[i])`


"""
from bisect import bisect_right
import sys

def check(arr1, arr2, x, k):
    less_or_equal_k_count = 0
    for val in arr1:
        less_or_equal_k_count += bisect_right(arr2, x - val)
        if less_or_equal_k_count >= k:  # Early exit optimization
            return True
    return less_or_equal_k_count >= k


def solve(a, b, k):
    """
    Return the `k` smallest number in `c` ( just index wise, not distinct)
    """
    if not a or not b:
        return -1  # Handle edge case where input arrays are empty
    
    if len(a) > len(b):  # Perform binary search on the smaller array
        a, b = b, a

    a.sort()
    b.sort()
    lo, hi = a[0] + b[0], a[-1] + b[-1]
    res = hi

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if check(a, b, mid, k):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    return res

a = [1,2,3]
b = [4,5,6]
k=6
# c = [5,6,6,7,7,7,8,8,9]


print(solve(a,b,k))