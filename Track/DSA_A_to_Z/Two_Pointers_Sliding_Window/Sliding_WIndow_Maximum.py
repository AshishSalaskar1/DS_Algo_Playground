"""
https://leetcode.com/submissions/detail/1840329638/

Classic sliding window + heap + lazy deletion
"""
from heapq import heapify, heappush, heappop

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        h = []
        removed = set()
        heapify(h)

        l,r = 0,0
        res = []
        while r<n:
            wsize = r-l+1
            heappush(h,(-arr[r],r))

            if wsize < k: r += 1
            else: # wsize match
                while h and h[0] in removed: heappop(h)

                res.append(-h[0][0])
                removed.add((-arr[l],l))

                l += 1
                r += 1

        return res


