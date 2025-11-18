"""
Subarrays with K Different Integers: https://leetcode.com/problems/subarrays-with-k-different-integers/


SOLUTION LOGIC:
- subarraysWithKDistinct is HARD TO FIND
- subarraysWithAtmostKDistinct is easier

so:
subarraysWithKDistinct(arr,k) = subarraysWithAtmostKDistinct(arr, k) - subarraysWithAtmostKDistinct(arr, k-1)

"""
class Solution:
    def subarraysWithKDistinct(self, arr: List[int], k: int) -> int:
        return self.subarraysWithAtmostKDistinct(arr,k)-self.subarraysWithAtmostKDistinct(arr,k-1)


    def subarraysWithAtmostKDistinct(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cmap = {}

        l,r = 0,0
        res = 0
        while r<n:
            cmap[arr[r]] = cmap.get(arr[r],0) + 1

            while l<=r and len(cmap) > k:
                cmap[arr[l]] -= 1
                if cmap[arr[l]] == 0: cmap.pop(arr[l])
                l += 1

            res += r-l  # EVERY VALID WINDOW
            r += 1

        return res
                
"""
class Solution:
    def subarraysWithKDistinct(self, arr: List[int], k: int) -> int:
        return self.subarraysWithAtmostKDistinct(arr,k)-self.subarraysWithAtmostKDistinct(arr,k-1)


    def subarraysWithAtmostKDistinct(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cmap = {}

        l,r = 0,0
        res = 0
        while r<n:
            cmap[arr[r]] = cmap.get(arr[r],0) + 1

            while l<=r and len(cmap) > k:
                cmap[arr[l]] -= 1
                if cmap[arr[l]] == 0: cmap.pop(arr[l])
                l += 1
            res += r-l
            r += 1

        return res
"""


        