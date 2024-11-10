"""
https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/description/
Maximum Frequency of an Element After Performing Operations I
"""

from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        events = []
        counter = Counter(nums)

        for x in nums:
            events.append( (x, 0) )
            events.append( (x-k, 1) )
            events.append( (x+k+1, -1) )

        events.sort()
        res = 0
        cur = 0

        for event in events:
            pos, delta = event
            cur += delta 

            # if you pick pos, for sure you will have counter[pos] matches
            # now remaining mathches = cur_count - counter[pos] (this cant be more than numOperations)
            # cur_count - counter[pos] (lets say you have 10 cur matches, but since after picking pos you already have counter[pos] taken)
            res = max(
                res,
                counter[pos] + min(cur-counter[pos], numOperations)
            )
        
        return res
        