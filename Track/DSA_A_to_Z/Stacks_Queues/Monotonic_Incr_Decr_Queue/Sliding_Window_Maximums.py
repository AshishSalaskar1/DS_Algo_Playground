"""
PROBLEM: https://leetcode.com/problems/sliding-window-maximum/description/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

SOLUTION:
- Brute force: O(n*k) - Iterate each window and find minimumg
- Can you use PQ? No (You dont always add/remove max value - it can be others also)
    - Q = [1,2,3], PQ = [3,1,2] => res=q.get() or q[0]
    - arr = [1,(2,3,4)] -> now here 4 came new
    - You need to remove 1 (No method to remove number by val in PQ)

- O(N) Solution: MONOTONICALL DECREASING DEQUE
- In this MDD: left most element will always be the max
- L=R=0 (left and right boundaries)
=> while r<n: keep on incrementing r
    -> keep on popping until stack.top() > arr[r]
    -> then push arr[r]
    -> Check if the left_most(max) element in Q is before Left
        - if YES, that means you need to popleft (that left most element which is max < LEFT)
    -> In any case if r-l+1 >= k: Update res with max (q[0])
"""

from collections import deque

class Ele:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = deque()
        res = []
        
        l,r = 0,0

        while r<n:
            # before inserting make sure all element in Q <= curr
            while len(q) != 0 and q[-1].val <= arr[r]:
                q.pop() # pop right
            q.append(Ele(r, arr[r]))

            # check if left needs to be popped (You have moved to next window)
            if l > q[0].idx:
                q.popleft()

            if r-l+1 >= k: # whenever your window size == k
                res.append(q[0].val)
                l += 1 # move to next window
            
            r += 1 # move to next element

        return res



