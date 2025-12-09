"""
https://leetcode.com/problems/count-special-triplets/description/?envType=daily-question&envId=2025-12-09

VALID: https://leetcode.com/problems/count-special-triplets/solutions/7401382/solve-all-prefix-suffix-problems-instant-2v3l
"""
from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def specialTriplets(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        freqnext, freqprev = defaultdict(int), defaultdict(int)
        
        # Add everything to seenlater
        for i,x in enumerate(arr):
            freqnext[x] = freqnext[x] + 1

        res = 0
        for x in arr:
            # remove current from seenLater
            freqnext[x] -= 1
            target = x*2

            res = (res + (freqnext[target]*freqprev[target]))%MOD

            # add current to SeenBefore
            freqprev[x] = freqprev[x]+1
        
        return res
