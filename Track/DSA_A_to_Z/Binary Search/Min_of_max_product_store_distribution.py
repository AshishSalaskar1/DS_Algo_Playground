"""
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/solutions/6042579/python-binary-search-pattern


SOLUTION:
- You are given quanitities of `Q` items
- You can distribute only 1 item to each store (you can allocate multiple of each item type)
- You have n stores
AIM: Minimize the max product quantity given to any store

SOLUTION:
res = 1 to max(Quantities)
- 1 : best case you assign 
- max(quantities): worst you can assign

for each res -> find number of stores needed such that if you distribute all items the max remains <res
= sum( ceil(quantity/res) for quantity in quantities )

Meaning: lets say my res=3, i can at max give each store 3 quantity
- now quantities = [11,6]
1. 11/3 = 9.x = 10 (You need atleast 10 stores to distribute item1 such that no store gets more than res)
2. 6/3 = 2 ((You need atleast 2 stores to distribute item1 such that no store gets more than res))
- In total you need 12 stores [CHECK IF YOU HAVE THESE MANY]
"""

import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo,hi = 1, max(quantities)
        res = float("inf")

        while lo <= hi:
            mid = lo + (hi-lo)//2
            # how many stores you need such that res = mid
            num_stores = sum([math.ceil(x/mid) for x in quantities])

            if num_stores <= n:
                res = min(res, mid)
                hi = mid-1
            else:
                lo = mid+1
        
        return res

        