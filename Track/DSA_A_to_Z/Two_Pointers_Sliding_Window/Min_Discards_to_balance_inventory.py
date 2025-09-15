"""
INTUTION:
- Simple sliding window approach with one big catch
1. You check if adding an element (r) -> voilates? If yes then dont pick it [ update count ONLY IF YOU PICK IT]
2. Then decide whether to shift window, or just increase it

CATCH:
- while shifting you cant just do l++, r++ and cmap[arr[l]] -= 1
WHY?
- Because you might have not kept [l], that means it was never counted -> SO NO NEED TO DECREASE IT


"""

from collections import defaultdict
from typing import List

class Solution:
    def minArrivalsToDiscard(self, arr: List[int], w: int, m: int) -> int:
        n = len(arr)

        cmap = defaultdict(int) 
        keep = [False] * n
        discards = 0

        l,r = 0,0

        while r<n:
            wsize = r-l+1

            # Can you take the current item?
            if cmap[arr[r]] >= m: # already has more than m
                keep[r] = False
                discards += 1
            else:
                cmap[arr[r]] += 1
                keep[r] = True

            
            if wsize < w: # increase window
                r += 1
            else: # shift window
                r += 1
                if keep[l]: # was l kept before?
                    cmap[arr[l]] -= 1
                l += 1

        return discards
                    
                
            
            