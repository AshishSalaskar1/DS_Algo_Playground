"""
Problem: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

Whenever you made a cut, its cost = length before cutting

Example:
- n = 7, cuts = [1,3,4,5], RES = 16

The first cut is done to a rod of length 7 so the cost is 7. 
The second cut is done to a rod of length 6 (i.e. the second part of the first cut), 
the third is done to a rod of length 4 and the last cut is to a rod of length 3. 

The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 


SOLUTION:
- Instead of going pure DP way -> cut at each possible point n see -> LETS USE PARTITION DP
- cuts[i] = cuts can be made at point i such that left part will be of length=i


=> PARTITION DP on CUTS
Ex: n = 7, cuts = [1,3,4,5], RES = 16

- SORT CUTS (Such that we can divide it into 2 independent problems)
    - [p1=[1,5],p2=[4,3]] -> here elements in p1 cut p2 and vice versa

- Pad cuts array: [0, *cuts, n] <- to get length of stick before cutting
    - WHY? Lets say you call fn(i,j) and then try all cuts possible in [i,j]
    - NOW, for [i,j] in cuts, 
        1. i-1: where was it last cut at left
        2. j+1: where was it last cut at right
        - Initially its like, cut at 0 and cut at n+1/n

    - You make cut at i+1, now you need the cost of that cut (length before cutting)
    - Base case: [0, i=1,3,4,j=5 , 7] -> fn(1,len(cuts))
        - Here, you make any cut but cost will be = 7 (len of array)
        - Length = cost = cuts[j+1] - cuts[i-1] = 7-1 = 1
    - Case 2: [0, 1,i=3,j=4,5 , 7] -> fn(2,3)
        - Here you make cut at 3 or 4, length = cost = 5-1 = 4
        - COST = Where was it last cut at right - Where was it last cut at left


- fn(i,j) -> PARTITION ON CUTS
    - You can cut at [i..j], i and j inclusive
    - In case you cut at k,
        # you cut and then you have two halves remaining
        cost = cuts[j+1]-cuts[i-1]
               + fn(i,k-1)
               + fn(k+1,j)

"""

from functools import cache
class Solution:
    @cache
    def fn(self, i, j) -> int:
        if i>j:
            return 0
        
        res = float("inf")
        for k in range(i,j+1):
            cost = self.cuts[j+1]-self.cuts[i-1]+self.fn(i,k-1)+self.fn(k+1,j)
            res = min(cost,res)
        
        return res
        
    def minCost(self, n: int, cuts: List[int]) -> int:
        # cuts = [1,3,4,5] -> [0, 1,3,4,5, 7]
        cuts = sorted(cuts)
        self.cuts = [0, *cuts, n]
        return self.fn(1,len(cuts)) # 1,5 -> [0, 1,3,4,5, 7]

        