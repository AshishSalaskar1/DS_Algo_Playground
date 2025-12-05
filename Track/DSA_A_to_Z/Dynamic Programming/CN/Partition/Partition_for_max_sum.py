"""
https://leetcode.com/problems/partition-array-for-maximum-sum/description/
"""
from functools import lru_cache
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)

        @lru_cache()
        def solve(i: int):
            if i == n:
                return 0
            
            best = 0
            maxele = 0
            for j in range(i,min(i+k,n)):
                maxele = max(maxele, arr[j])
                winlen = j-i+1
                best = max(
                    best,
                    (winlen*maxele) + solve(j+1)
                )

            return best
           
        
        return solve(0)
    

print("Hello World")