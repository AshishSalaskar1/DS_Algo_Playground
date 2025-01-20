"""
PROBLEM: https://leetcode.com/problems/continuous-subarrays/
STATEMENT: Given an array find count all of all subarray such that Absolute Difference b/w any pairs in that subarray <= (k=2)


SOLUTION:
- if abs(min(arr)-max(arr))<=k -> THEN SURELY THE DIFFERNCES OF ANY PAIRS IN IT <=k
- Same logic as two pointer template, but here we increment `l` within `r` and not `r`
    - To increment `r`, you will first have to add it PQs, check and then move if correct (else remove from PQ)
    - For other template problems, you could directly compare whether `r+1` can be taken or not (DISTINCT, SUM etc)

- While popping the element why u blindly pop all on top < index? Can elements with index not lie beneath top?
ANS: No, since now left is incremented only if it voilates => min and max will also violate n lie on top (they voilated was the reason why you incremented l )
ANOTHER QUESTION -> Find largest such subarray

"""
from queue import PriorityQueue
from typing import List

class Solution:
    def continuousSubarrays(self, arr: List[int]) -> int:
        k = 2  # Maximum allowed difference between min and max
        minh = PriorityQueue()  # Min heap
        maxh = PriorityQueue()  # Max heap
        n = len(arr)
        l, r = 0, -1  # Sliding window boundaries
        result = 0  # To count the number of valid subarrays

        while r < n - 1:
            # Expand the window
            r += 1
            minh.put((arr[r], r))
            maxh.put((-arr[r], r))

            # INCREMENT LEFT ONLY IF IT VOILATES
            while abs(minh.queue[0][0] - (-maxh.queue[0][0])) > k:
                # Contract the window from the left
                l += 1

                # Remove elements outside the window from heaps
                while not minh.empty() and minh.queue[0][1] < l:
                    minh.get()
                while not maxh.empty() and maxh.queue[0][1] < l:
                    maxh.get()

            # Count all valid subarrays ending at index `r`
            print(f"{l} -> {r}")
            result += (r - l + 1)

        return result
