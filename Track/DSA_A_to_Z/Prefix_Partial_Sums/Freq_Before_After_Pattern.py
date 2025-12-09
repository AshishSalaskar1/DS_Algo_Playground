"""
https://leetcode.com/problems/count-special-triplets/description/?envType=daily-question&envId=2025-12-09
VALID: https://leetcode.com/problems/count-special-triplets/solutions/7401382/solve-all-prefix-suffix-problems-instant-2v3l
"""
from collections import defaultdict

class Solution:
    def specialTriplets(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        fafter, fbefore = defaultdict(int), defaultdict(int)
        for i,x in enumerate(arr):
            fafter[x] += 1

        res = 0
        for x in arr:
            # remove current from seenLater
            fafter[x] -= 1
            target = x*2

            res = (res + (fafter[target]*fbefore[target]))%MOD

            # add current to SeenBefore
            fbefore[x] += 1
        
        return res



# https://leetcode.com/problems/number-of-ways-to-select-buildings/
from collections import defaultdict
class Solution:
    def numberOfWays(self, s: str) -> int:
        s = [int(x) for x in s]
        fafter, fbefore = defaultdict(int), defaultdict(int)

        for x in s:
            fafter[x] += 1
        
        res = 0
        for x in s:
            fafter[x] -= 1
            
            if x==0: res += (fbefore[1]*fafter[1])
            else: res += (fbefore[0]*fafter[0])

            fbefore[x] += 1
        
        return res
        