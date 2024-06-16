"""
PROBLEM: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/

DETAILED SOLUTION: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/solutions/5320206/dynamic-programming-solution-sort-optimized-o-n-dp-python-c

INTUITIONS
- dp[i] = max spells profit you can make until i
- At index i, you have 2 options
    1) Pick spell i: cost = prev_best + arr[i]*count[arr[i]]
        - prev_best = first element from L<-R which is < x-2
    2) Dont pick: cost = dp[i-1]
    dp[i] = max(1, 2)

- HINT: if you have x spells of same power ( you will always pick all thats why (1) arr[i]*count[arr[i]])

"""
from collections import Counter
class Solution:
    def maximumTotalDamage(self, arr: List[int]) -> int:
        n = len(arr)
        arr_count = Counter(arr)

        arr = sorted(arr_count.keys())
        dp = [0] * len(arr)

        for i, x in enumerate(arr):
            prev_best = 0
            
            # find prev best -> first element from L<-R which is < x-2
            j = i-1
            while j>=0 and arr[j] >= (x-2):
                j -= 1
            if j>=0: 
                prev_best = dp[j]
            
            score_picking_current = x*arr_count[x] + prev_best
            score_not_picking_current = dp[i-1]
            dp[i] = max(score_picking_current, score_not_picking_current)
        
        return dp[-1]


        
