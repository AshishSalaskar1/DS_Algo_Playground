"""
https://leetcode.com/submissions/detail/1840329638/

Classic sliding window + heap + lazy deletion

LAZY DELETION: 
When we pop from heap, we check if the index is still in the window. If not, we pop again until we find a valid element.
This avoids the need to remove elements
"""
from heapq import heapify, heappush, heappop

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        h = []
        heapify(h)

        l,r = 0,0
        res = []
        while r<n:
            wsize = r-l+1
            heappush(h,(-arr[r],r))

            if wsize < k: r += 1
            else: # wsize match
                while h and (h[0][1]>r or h[0][1]<l): heappop(h)

                res.append(-h[0][0])

                l += 1
                r += 1

        return res





