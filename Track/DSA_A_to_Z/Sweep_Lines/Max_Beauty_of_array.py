"""
Maximum Beauty of an Array After Applying Operation

https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/?envType=daily-question&envId=2024-12-11

Solution: Sweepline
"""
class Solution:
    def maximumBeauty(self, arr: List[int], k: int) -> int:
        n = len(arr)
        events = []
        
        for i, val in enumerate(arr):
            events.append((val-k, 1))
            events.append((val+k+1, -1))
        
        events.sort(key=lambda x:(x[0],x[1]))
        max_count, count = 0, 0

        for index, incr in events:
            count += incr
            max_count = max(max_count, count)
        
        return max_count





        